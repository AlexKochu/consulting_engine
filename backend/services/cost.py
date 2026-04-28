import os
import pandas as pd
from utils.helpers import clean_data, format_currency

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

def analyze_cost_reduction(industry, current_costs):
    """
    Analyzes cost structure against benchmarks.
    current_costs is a dict: {'COGS': float, 'Marketing': float, ...}
    Values are current spend in dollars or percent of revenue. We assume dollars here.
    """
    df = pd.read_csv(os.path.join(DATA_DIR, 'cost.csv'))
    
    # Filter by industry
    industry_data = df[df['industry'] == industry]
    if industry_data.empty:
        industry_data = df
        
    total_current_cost = sum(current_costs.values())
    
    results = []
    total_savings_potential = 0
    
    chart_data = {
        'categories': [],
        'current_pct': [],
        'benchmark_pct': []
    }
    
    for category, amount in current_costs.items():
        if total_current_cost == 0:
            continue
            
        current_pct = (amount / total_current_cost) * 100
        
        # Get benchmark
        cat_data = industry_data[industry_data['cost_category'] == category]
        if not cat_data.empty:
            bench_pct = cat_data['benchmark_percent'].mean()
        else:
            # Fallback benchmark
            bench_pct = 15.0
            
        variance = current_pct - bench_pct
        is_inefficient = variance > 2.0 # 2% threshold
        
        savings_potential = 0
        if is_inefficient:
            # If we reduce to benchmark, how much $ do we save?
            target_cost = total_current_cost * (bench_pct / 100)
            savings_potential = amount - target_cost
            total_savings_potential += savings_potential
            
        results.append({
            'category': category,
            'current_spend': amount,
            'current_pct': round(current_pct, 1),
            'benchmark_pct': round(bench_pct, 1),
            'variance_pct': round(variance, 1),
            'is_inefficient': is_inefficient,
            'savings_potential': round(savings_potential, 2)
        })
        
        chart_data['categories'].append(category)
        chart_data['current_pct'].append(round(current_pct, 1))
        chart_data['benchmark_pct'].append(round(bench_pct, 1))
        
    # Sort results by savings potential descending
    results = sorted(results, key=lambda x: x['savings_potential'], reverse=True)
    
    savings_pct = (total_savings_potential / total_current_cost * 100) if total_current_cost > 0 else 0
    confidence_score = min(99, int(60 + savings_pct)) if savings_pct > 0 else 85
    
    if results and total_savings_potential > 0:
        drivers = [results[0]['category']]
        if len(results) > 1:
            drivers.append(results[1]['category'])
        else:
            drivers.append(results[0]['category'])
            
        primary_recommendation = f"Reduce {drivers[0]} to meet industry benchmarks"
        secondary_recommendation = f"Audit {drivers[1]} for further efficiency" if len(results) > 1 else ""
        trade_offs = f"Reducing {drivers[0]} improves margins but may impact operational efficiency or service quality."
        sensitivity = f"If labor or materials for {drivers[0]} increase, savings opportunities may shift."
        business_impact = f"Realizing these savings improves total margin by reducing spend by {format_currency(total_savings_potential)}."
        
        top_score = results[0]['savings_potential']
        second_score = results[1]['savings_potential'] if len(results) > 1 else (top_score * 0.5)
        confidence_score = round((top_score / (top_score + second_score)) * 100, 1) if (top_score + second_score) > 0 else 50.0
    else:
        drivers = ["All categories", "Efficiency maximized"]
        primary_recommendation = "Maintain current cost structure"
        secondary_recommendation = ""
        trade_offs = "Current structure is highly optimized to industry standards."
        sensitivity = "Market conditions or inflation could require future adjustments."
        business_impact = "No immediate cost reduction needed."
        confidence_score = 85.0
        
    why_it_matters = "This reduces unnecessary spend while protecting operational efficiency."

    result = {
        'total_analyzed': total_current_cost,
        'formatted_total_analyzed': format_currency(total_current_cost),
        'total_savings_potential': round(total_savings_potential, 2),
        'formatted_total_savings_potential': format_currency(total_savings_potential),
        'savings_pct': round(savings_pct, 1),
        'breakdown': results,
        'chart_data': chart_data,
        'primary_recommendation': primary_recommendation,
        'secondary_recommendation': secondary_recommendation,
        'why_it_matters': why_it_matters,
        'confidence_score': confidence_score,
        'drivers': drivers,
        'trade_offs': trade_offs,
        'sensitivity': sensitivity,
        'business_impact': business_impact
    }
    
    return clean_data(result)
