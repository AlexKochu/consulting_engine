import json
from flask import Blueprint, render_template, request, Response
from services.pricing import analyze_pricing
from services.market import analyze_market_entry
from services.cost import analyze_cost_reduction
from services.llm_service import generate_insights
from utils.report_generator import generate_html_report

main = Blueprint('main', __name__)

@main.route('/')
def landing():
    return render_template('landing.html')

@main.route('/app')
def app_index():
    return render_template('index.html')

@main.route('/analyze', methods=['POST'])
def analyze():
    problem_type = request.form.get('problem_type')
    
    try:
        if problem_type == 'pricing':
            industry = request.form.get('industry')
            try:
                current_price = float(request.form.get('current_price'))
                current_cost = float(request.form.get('current_cost'))
            except (ValueError, TypeError):
                return render_template('index.html', error="Price and Cost must be valid numbers.")
                
            if current_price <= 0 or current_cost <= 0 or current_price > 1e7 or current_cost > 1e7:
                return render_template('index.html', error="Price and Cost must be greater than 0 and less than 10M.")
            
            data = analyze_pricing(industry, current_price, current_cost)
            insights = generate_insights("Pricing Strategy", data)
            
        elif problem_type == 'market':
            try:
                growth = float(request.form.get('weight_growth'))
                demand = float(request.form.get('weight_demand'))
                comp = float(request.form.get('weight_competition'))
                income = float(request.form.get('weight_income'))
            except (ValueError, TypeError):
                return render_template('index.html', error="Market weights must be valid numbers.")
            
            weights = {'growth': growth, 'demand': demand, 'competition': comp, 'income': income}
            data = analyze_market_entry(weights)
            insights = generate_insights("Market Entry", data)
            
        elif problem_type == 'cost':
            industry = request.form.get('industry')
            try:
                cogs = float(request.form.get('cost_cogs') or 0)
                marketing = float(request.form.get('cost_marketing') or 0)
                rnd = float(request.form.get('cost_rnd') or 0)
                admin = float(request.form.get('cost_admin') or 0)
                it = float(request.form.get('cost_it') or 0)
            except (ValueError, TypeError):
                return render_template('index.html', error="Costs must be valid numbers.")
                
            if any(c < 0 or c > 1e9 for c in [cogs, marketing, rnd, admin, it]):
                return render_template('index.html', error="Costs cannot be negative or exceed 1B.")
            
            costs = {'COGS': cogs, 'Marketing': marketing, 'R&D': rnd, 'Admin': admin, 'IT Infrastructure': it}
            costs = {k: v for k, v in costs.items() if v > 0}
            
            data = analyze_cost_reduction(industry, costs)
            insights = generate_insights("Cost Reduction", data)
            
        else:
            return render_template('index.html', error="Invalid problem type selected.")
            
        return render_template(
            'result.html', 
            problem_type=problem_type,
            data=data,
            insights=insights,
            chart_data_json=json.dumps(data.get('chart_data', {})),
            data_json=json.dumps(data),
            insights_json=json.dumps(insights)
        )
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        return render_template('index.html', error=f"An error occurred: {str(e)}")

@main.route('/download_report', methods=['POST'])
def download_report():
    problem_type = request.form.get('problem_type')
    data = json.loads(request.form.get('data'))
    insights = json.loads(request.form.get('insights'))
    
    html_content = generate_html_report(problem_type, data, insights)
    
    return Response(
        html_content,
        mimetype="text/html",
        headers={"Content-disposition": f"attachment; filename={problem_type}_report.html"}
    )
