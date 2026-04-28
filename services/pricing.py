import os
import pandas as pd
import numpy as np
from utils.helpers import clean_data, format_currency

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

def analyze_pricing(industry, current_price, current_cost):
    """
    Analyzes pricing for a given industry.
    Returns optimal price, revenue curve data, and summary metrics.
    """
    df = pd.read_csv(os.path.join(DATA_DIR, 'pricing.csv'))
    
    # Filter by industry
    industry_data = df[df['industry'] == industry]
    if industry_data.empty:
        # Fallback to general market if not found
        industry_data = df
        
    avg_elasticity = industry_data['elasticity'].mean()
    base_demand = industry_data['demand_index'].mean()
    
    # Define a price range to simulate
    min_sim_price = max(current_cost * 1.1, current_price * 0.5)
    max_sim_price = current_price * 1.5
    price_points = np.linspace(min_sim_price, max_sim_price, 50)
    
    results = []
    optimal_price = current_price
    max_profit = -float('inf')
    
    current_demand = base_demand
    current_revenue = current_price * current_demand
    current_profit = (current_price - current_cost) * current_demand
    
    for p in price_points:
        # Calculate percentage change in price
        price_change_pct = (p - current_price) / current_price
        
        # Calculate new demand using elasticity (E = % change in Q / % change in P)
        demand_change_pct = avg_elasticity * price_change_pct
        
        # Simulated demand (can't be negative)
        sim_demand = max(0, base_demand * (1 + demand_change_pct))
        
        revenue = p * sim_demand
        profit = (p - current_cost) * sim_demand
        
        results.append({
            'price': round(p, 2),
            'demand': round(sim_demand, 0),
            'revenue': round(revenue, 2),
            'profit': round(profit, 2)
        })
        
        if profit > max_profit:
            max_profit = profit
            optimal_price = p
            
    # Format curve data for Plotly
    curve_data = {
        'prices': list([r['price'] for r in results]),
        'revenues': list([r['revenue'] for r in results]),
        'profits': list([r['profit'] for r in results])
    }
    
    # Summary of current vs optimal
    profit_increase_pct = ((max_profit - current_profit) / current_profit * 100) if current_profit > 0 else 0
    
    price_difference = optimal_price - current_price
    profit_comparison = max_profit - current_profit
    
    # Generate deterministic drivers
    drivers = []
    if price_difference < -0.01:
        drivers.append("Price is too high relative to demand elasticity in this industry.")
        drivers.append("Demand sensitivity indicates lowering price increases volume and total profit.")
    elif price_difference > 0.01:
        drivers.append("Demand is relatively inelastic in this segment.")
        drivers.append("Current pricing leaves margin on the table; higher price compensates for minor volume drop.")
    else:
        drivers.append("Current price is already perfectly optimized for demand elasticity.")
        
    # Generate business impact statement
    if profit_comparison > 0:
        if price_difference < 0:
            business_impact = f"Reducing price will capture more volume, increasing overall profit by {format_currency(profit_comparison)}."
            primary_recommendation = f"Decrease price to {format_currency(optimal_price)}"
            secondary_recommendation = "Maintain current price if operational volume capacity is restricted."
            trade_offs = "Lowering price increases volume and total profit, but reduces per-unit margin."
            sensitivity = "If demand becomes less elastic, maintaining a higher price will be optimal."
        else:
            business_impact = f"Increasing price will improve margins, raising overall profit by {format_currency(profit_comparison)}."
            primary_recommendation = f"Increase price to {format_currency(optimal_price)}"
            secondary_recommendation = "Execute gradual price hikes to test customer churn."
            trade_offs = "Higher prices improve per-unit margin but will likely result in a minor volume drop."
            sensitivity = "If market competition intensifies, a price increase may lead to higher-than-expected churn."
    else:
        business_impact = "No significant profit increase available through price changes."
        primary_recommendation = "Maintain current price"
        secondary_recommendation = ""
        trade_offs = "Current price perfectly balances volume and margin."
        sensitivity = "Monitor competitor pricing; any market shift will require recalculation."
        
    top_score = max_profit
    second_score = current_profit
    confidence_score = round((top_score / (top_score + second_score)) * 100, 1) if (top_score + second_score) > 0 else 50.0

    why_it_matters = "This adjustment captures price-sensitive demand, increasing total profit."

    result = {
        'optimal_price': round(optimal_price, 2),
        'max_profit': round(max_profit, 2),
        'profit_increase_pct': round(profit_increase_pct, 2),
        'avg_elasticity': round(avg_elasticity, 2),
        'current_price': round(current_price, 2),
        'current_profit': round(current_profit, 2),
        'price_difference': round(price_difference, 2),
        'formatted_optimal_price': format_currency(optimal_price),
        'formatted_current_price': format_currency(current_price),
        'formatted_price_difference': format_currency(price_difference),
        'profit_comparison': round(profit_comparison, 2),
        'drivers': drivers,
        'business_impact': business_impact,
        'primary_recommendation': primary_recommendation,
        'secondary_recommendation': secondary_recommendation,
        'why_it_matters': why_it_matters,
        'confidence_score': float(confidence_score),
        'trade_offs': trade_offs,
        'sensitivity': sensitivity,
        'curve_data': curve_data
    }
    
    return clean_data(result)
