import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# We are using Groq with OpenAI compatible client
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def generate_insights(problem_type, data_dict):
    """
    Takes deterministic output and uses LLM to generate narrative.
    """
    prompt = f"""
    You are a senior McKinsey-style strategy consultant. Based ONLY on the following data analysis for a {problem_type} strategy, provide a sharp, highly analytical, and business-focused explanation.
    Do NOT perform mathematical calculations. Use the exact numbers and drivers provided.
    Do NOT use emojis, filler words, or generic phrasing (e.g., "leveraging insights", "rigorously benchmarked"). Be concise, direct, and realistic.
    
    Data:
    {json.dumps(data_dict, indent=2)}
    
    Return the response in the following JSON structure EXACTLY:
    {{
        "executive_summary": "Concise 1-2 sentence high-level summary of the analysis.",
        "current_situation": "Analytical explanation of current metrics and strategic alignment.",
        "key_insight": "The single most critical driver, variance, or elasticity discovered.",
        "recommendation": "Direct, clear strategic action to take.",
        "business_impact": "Quantifiable effect on profit, margins, or market capture.",
        "risks_and_next_steps": ["Concise risk 1", "Concise risk 2", "Immediate next step 1"]
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a senior strategy consultant. Output sharp, analytical, valid JSON only. No emojis. No fluff."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.2
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        print(f"LLM Error: {e}")
        # Fallback if API fails (Deterministic professional text)
        return {
            "executive_summary": f"Data-driven evaluation completed for {problem_type} strategy. Deterministic drivers highlight actionable strategic shifts.",
            "current_situation": "Current metrics indicate misalignment with optimal market positioning.",
            "key_insight": "Primary strategic drivers dictate a shift to capture identified value.",
            "recommendation": "Execute the primary decision listed in the strategic diagnosis.",
            "business_impact": "Implementation will optimize positioning and capture projected margin or market share.",
            "risks_and_next_steps": [
                "Market volatility may accelerate faster than historical models predict.", 
                "Execution risk remains the primary constraint.", 
                "Validate internal capacity before implementation."
            ]
        }
