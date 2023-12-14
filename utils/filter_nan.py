import json
import math

def replace_nan_with_zero(data):
    """
    Recursively process the data to replace NaN values with zero.
    """
    if isinstance(data, dict):
        return {k: replace_nan_with_zero(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_nan_with_zero(v) if not (isinstance(v, float) and math.isnan(v)) else 0 for v in data]
    else:
        return data

# Load the data
with open('./data/zc_nasbench201_layerwise.json', 'r') as file:
    data = json.load(file)

# Replace NaN values with zero
processed_data = replace_nan_with_zero(data)

# Write the processed data back to a file
with open('./data/processed_zc_nasbench201_layerwise.json', 'w') as file:
    json.dump(processed_data, file, indent=4)
