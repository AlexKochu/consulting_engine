import os
import pandas as pd
import numpy as np

# Ensure data directory exists
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def generate_pricing_data(n_rows=50):
    """
    Generates synthetic data for pricing logic.
    industry, avg_price, min_price, max_price, elasticity, competitor_price, demand_index
    """
    np.random.seed(42)
    industries = ['SaaS', 'E-commerce', 'Hardware', 'Services', 'Consulting']
    
    data = []
    for _ in range(n_rows):
        industry = np.random.choice(industries)
        # Base price depends on industry
        base = {'SaaS': 50, 'E-commerce': 100, 'Hardware': 500, 'Services': 200, 'Consulting': 1000}[industry]
        
        avg_price = np.round(np.random.normal(base, base * 0.2), 2)
        min_price = np.round(avg_price * 0.7, 2)
        max_price = np.round(avg_price * 1.5, 2)
        
        # Elasticity: negative value, typically between -0.5 and -2.5
        elasticity = np.round(np.random.uniform(-2.5, -0.5), 2)
        
        competitor_price = np.round(np.random.normal(avg_price, avg_price * 0.1), 2)
        
        # Base demand index, varied
        demand_index = np.round(np.random.uniform(500, 5000))
        
        data.append([industry, avg_price, min_price, max_price, elasticity, competitor_price, demand_index])
        
    df = pd.DataFrame(data, columns=['industry', 'avg_price', 'min_price', 'max_price', 'elasticity', 'competitor_price', 'demand_index'])
    
    # Introduce some logical variance
    df.loc[df['elasticity'] < -1.5, 'demand_index'] *= 1.2 # Highly elastic markets might have larger absolute demand
    
    df.to_csv(os.path.join(DATA_DIR, 'pricing.csv'), index=False)
    print("Generated pricing.csv")


def generate_market_data(n_rows=50):
    """
    Generates synthetic data for market entry.
    region, market_size, growth_rate, competition_level, avg_income, demand_score, urbanization
    """
    np.random.seed(43)
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East']
    
    data = []
    for _ in range(n_rows):
        region = np.random.choice(regions)
        
        # Market size in millions
        market_size = np.round(np.random.uniform(10, 500), 1)
        
        # Growth rate percentage (can be negative but mostly positive)
        growth_rate = np.round(np.random.normal(5.0, 3.0), 1)
        
        # Competition level (1-10)
        competition_level = np.random.randint(1, 11)
        
        # Avg income correlates slightly with region
        base_income = {'North America': 60000, 'Europe': 45000, 'Asia Pacific': 25000, 'Latin America': 15000, 'Middle East': 30000}[region]
        avg_income = np.round(np.random.normal(base_income, base_income * 0.3))
        
        # Demand score (1-100)
        demand_score = np.round(np.clip(np.random.normal(50 + growth_rate * 2, 15), 1, 100))
        
        # Urbanization percentage
        urbanization = np.round(np.random.uniform(30, 95), 1)
        
        # Logic rule: High competition often means high market size
        if market_size > 300:
            competition_level = min(10, competition_level + 3)
            
        data.append([region, market_size, growth_rate, competition_level, avg_income, demand_score, urbanization])
        
    df = pd.DataFrame(data, columns=['region', 'market_size', 'growth_rate', 'competition_level', 'avg_income', 'demand_score', 'urbanization'])
    
    # Add noise to prevent perfect linear correlations
    df['demand_score'] += np.random.normal(0, 5, n_rows)
    df['demand_score'] = df['demand_score'].clip(1, 100).round()
    
    df.to_csv(os.path.join(DATA_DIR, 'market.csv'), index=False)
    print("Generated market.csv")


def generate_cost_data(n_rows=50):
    """
    Generates synthetic data for cost reduction.
    industry, cost_category, avg_percent, benchmark_percent, variance_flag
    """
    np.random.seed(44)
    industries = ['Manufacturing', 'Retail', 'Tech', 'Healthcare', 'Logistics']
    categories = ['COGS', 'Marketing', 'R&D', 'Admin', 'IT Infrastructure']
    
    data = []
    for _ in range(n_rows):
        industry = np.random.choice(industries)
        category = np.random.choice(categories)
        
        # Typical benchmark depends on category
        base_bench = {'COGS': 40, 'Marketing': 15, 'R&D': 10, 'Admin': 15, 'IT Infrastructure': 10}[category]
        benchmark_percent = np.round(np.random.normal(base_bench, base_bench * 0.1), 1)
        
        # Actual avg percent for this entity
        avg_percent = np.round(np.random.normal(benchmark_percent + 2, 5), 1) 
        # Clip to ensure valid percentages
        avg_percent = max(1.0, avg_percent)
        benchmark_percent = max(1.0, benchmark_percent)
        
        # Flag if variance is over 10% relatively higher than benchmark
        variance_flag = 1 if avg_percent > benchmark_percent * 1.1 else 0
        
        data.append([industry, category, avg_percent, benchmark_percent, variance_flag])
        
    df = pd.DataFrame(data, columns=['industry', 'cost_category', 'avg_percent', 'benchmark_percent', 'variance_flag'])
    df.to_csv(os.path.join(DATA_DIR, 'cost.csv'), index=False)
    print("Generated cost.csv")


if __name__ == "__main__":
    print("Generating datasets...")
    generate_pricing_data(50)
    generate_market_data(60)
    generate_cost_data(55)
    print("Done!")
