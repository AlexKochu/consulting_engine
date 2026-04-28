import numpy as np

def clean_data(data):
    """
    Recursively converts NumPy data types to native Python types
    to avoid JSON serialization errors ('Object of type bool_ is not JSON serializable').
    """
    if isinstance(data, dict):
        return {k: clean_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [clean_data(v) for v in data]
    elif isinstance(data, np.bool_):
        return bool(data)
    elif isinstance(data, np.integer):
        return int(data)
    elif isinstance(data, np.floating):
        return float(data)
    else:
        return data

def format_currency(value):
    """Formats large numbers into readable string representation ($X.XXM)."""
    if value is None:
        return "$0.00"
    if value >= 1e9:
        return f"${value/1e9:.2f}B"
    elif value >= 1e6:
        return f"${value/1e6:.2f}M"
    elif value >= 1e3:
        return f"${value/1e3:.2f}K"
    return f"${value:.2f}"
