import json
from flask import Blueprint, request, jsonify, Response
from services.pricing import analyze_pricing
from services.market import analyze_market_entry
from services.cost import analyze_cost_reduction
from services.llm_service import generate_insights
from utils.report_generator import generate_html_report

main = Blueprint('main', __name__)

@main.route('/health')
def health_check():
    return jsonify({"status": "ok"})

@main.route('/analyze', methods=['POST'])
def analyze():
    # Attempt to get JSON first, fallback to form data
    if request.is_json:
        payload = request.get_json()
    else:
        payload = request.form

    problem_type = payload.get('problem_type')
    print(f"DEBUG PAYLOAD: {payload}")
    
    try:
        if problem_type == 'pricing':
            industry = payload.get('pricing_industry')
            try:
                current_price = float(payload.get('current_price'))
                current_cost = float(payload.get('current_cost'))
            except (ValueError, TypeError):
                return jsonify({"error": "Price and Cost must be valid numbers."}), 400
                
            if current_price <= 0 or current_cost <= 0 or current_price > 1e7 or current_cost > 1e7:
                return jsonify({"error": "Price and Cost must be greater than 0 and less than 10M."}), 400
            
            data = analyze_pricing(industry, current_price, current_cost)
            insights = generate_insights("Pricing Strategy", data)
            
        elif problem_type == 'market':
            try:
                growth = float(payload.get('weight_growth'))
                demand = float(payload.get('weight_demand'))
                comp = float(payload.get('weight_competition'))
                income = float(payload.get('weight_income'))
            except (ValueError, TypeError):
                return jsonify({"error": "Market weights must be valid numbers."}), 400
            
            weights = {'growth': growth, 'demand': demand, 'competition': comp, 'income': income}
            data = analyze_market_entry(weights)
            insights = generate_insights("Market Entry", data)
            
        elif problem_type == 'cost':
            industry = payload.get('cost_industry')
            try:
                cogs = float(payload.get('cost_cogs') or 0)
                marketing = float(payload.get('cost_marketing') or 0)
                rnd = float(payload.get('cost_rnd') or 0)
                admin = float(payload.get('cost_admin') or 0)
                it = float(payload.get('cost_it') or 0)
            except (ValueError, TypeError):
                return jsonify({"error": "Costs must be valid numbers."}), 400
                
            total_cost = cogs + marketing + rnd + admin + it
            if total_cost <= 0:
                return jsonify({"error": "You must provide at least one cost value greater than 0."}), 400
                
            if any(c < 0 or c > 1e9 for c in [cogs, marketing, rnd, admin, it]):
                return jsonify({"error": "Costs cannot be negative or exceed 1B."}), 400
            
            costs = {'COGS': cogs, 'Marketing': marketing, 'R&D': rnd, 'Admin': admin, 'IT Infrastructure': it}
            costs = {k: v for k, v in costs.items() if v > 0}
            
            data = analyze_cost_reduction(industry, costs)
            insights = generate_insights("Cost Reduction", data)
            
        else:
            return jsonify({"error": "Invalid problem type selected."}), 400
            
        return jsonify({
            "success": True,
            "problem_type": problem_type,
            "data": data,
            "insights": insights
        })
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@main.route('/download_report', methods=['POST'])
def download_report():
    if request.is_json:
        payload = request.get_json()
        problem_type = payload.get('problem_type')
        data = payload.get('data')
        insights = payload.get('insights')
    else:
        problem_type = request.form.get('problem_type')
        data = json.loads(request.form.get('data'))
        insights = json.loads(request.form.get('insights'))
    
    html_content = generate_html_report(problem_type, data, insights)
    
    return Response(
        html_content,
        mimetype="text/html",
        headers={"Content-disposition": f"attachment; filename={problem_type}_report.html"}
    )
