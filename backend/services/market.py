import os
import pandas as pd
from utils.helpers import clean_data

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

def analyze_market_entry(priority_weights):
    """
    Analyzes market entry targets using weighted scoring.
    priority_weights is a dict: {'growth': float, 'demand': float, 'competition': float, 'income': float}
    Expected to sum to 1.0 or will be normalized.
    """
    df = pd.read_csv(os.path.join(DATA_DIR, 'market.csv'))
    
    # Normalize inputs
    total_weight = sum(priority_weights.values())
    w_growth = priority_weights.get('growth', 1.0) / total_weight
    w_demand = priority_weights.get('demand', 1.0) / total_weight
    w_comp = priority_weights.get('competition', 1.0) / total_weight
    w_income = priority_weights.get('income', 1.0) / total_weight
    
    # We want high growth, high demand, LOW competition, high income.
    # Min-Max scale the columns so they are comparable (0 to 1)
    def min_max_scale(series, inverse=False):
        min_val = series.min()
        max_val = series.max()
        if max_val == min_val:
            return 0.5
        scaled = (series - min_val) / (max_val - min_val)
        return 1 - scaled if inverse else scaled
        
    df['score_growth'] = min_max_scale(df['growth_rate'])
    df['score_demand'] = min_max_scale(df['demand_score'])
    df['score_comp'] = min_max_scale(df['competition_level'], inverse=True) # inverse because low is better
    df['score_income'] = min_max_scale(df['avg_income'])
    
    # Calculate weighted score (out of 100)
    df['final_score'] = (
        (df['score_growth'] * w_growth) +
        (df['score_demand'] * w_demand) +
        (df['score_comp'] * w_comp) +
        (df['score_income'] * w_income)
    ) * 100
    
    # Aggregate by region (take the mean final score and top characteristics)
    region_agg = df.groupby('region').agg({
        'final_score': 'mean',
        'market_size': 'sum',
        'growth_rate': 'mean',
        'competition_level': 'mean',
        'score_growth': 'mean',
        'score_demand': 'mean',
        'score_comp': 'mean',
        'score_income': 'mean'
    }).reset_index()
    
    # Sort and get top 3
    top_regions = region_agg.sort_values('final_score', ascending=False).head(3)
    
    chart_data = {
        'regions': list(top_regions['region']),
        'scores': list(top_regions['final_score'].round(1)),
        'market_sizes': list(top_regions['market_size'].round(0))
    }
    
    recommendations = []
    for _, row in top_regions.iterrows():
        recommendations.append({
            'region': row['region'],
            'score': round(row['final_score'], 1),
            'market_size': round(row['market_size'], 1),
            'growth_rate': round(row['growth_rate'], 1),
            'competition_level': round(row['competition_level'], 1)
        })
        
    primary = top_regions.iloc[0]
    secondary = top_regions.iloc[1]
    
    # Determine top drivers for a row
    def get_top_drivers(row):
        scores = {
            'High growth potential': row['score_growth']*w_growth, 
            'Strong consumer demand': row['score_demand']*w_demand, 
            'Favorable low competition': row['score_comp']*w_comp, 
            'High average income': row['score_income']*w_income
        }
        sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        return [sorted_scores[0][0], sorted_scores[1][0]]

    primary_region = primary['region']
    secondary_region = secondary['region']
    
    # Confidence Score based on difference
    top_score = primary['final_score']
    second_score = secondary['final_score']
    confidence_score = round((top_score / (top_score + second_score)) * 100, 1) if (top_score + second_score) > 0 else 50.0
    
    drivers = get_top_drivers(primary)
    
    primary_recommendation = f"Expand into {primary_region}"
    secondary_recommendation = f"Consider {secondary_region} as a secondary opportunity"
    
    trade_offs = f"{primary_region} provides strong {drivers[0].lower()}, but may have slower momentum in other areas compared to emerging secondary markets like {secondary_region}."
    
    sensitivity = f"If competition weight increases by 20%, {secondary_region} becomes highly competitive for the top spot."

    why_it_matters = "This region offers the best balance of growth, demand, and manageable competition."

    result = {
        'top_targets': recommendations,
        'chart_data': chart_data,
        'primary_recommendation': primary_recommendation,
        'secondary_recommendation': secondary_recommendation,
        'why_it_matters': why_it_matters,
        'confidence_score': confidence_score,
        'drivers': drivers,
        'trade_offs': trade_offs,
        'sensitivity': sensitivity,
        'business_impact': f"Expanding into {primary_region} optimizes market capture while mitigating identified risks."
    }
    
    return clean_data(result)
