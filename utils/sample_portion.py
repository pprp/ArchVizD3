import json
import random

# Assuming the JSON file contains a dictionary and not a list
# Updated the function to handle both cases (dictionary and list)

def sample_json(file_path, portion=0.2):
    """
    Samples a small portion from a JSON file.

    :param file_path: Path to the JSON file
    :param portion: Fraction of items to sample from the JSON (0.2 = 20%)
    :return: Sampled portion of the JSON file
    """
    with open(file_path, 'r') as file:
        data = json.load(file)['cifar10']

        # Check if data is a dictionary or a list
        if isinstance(data, dict):
            print(len(data))
            sample_size = int(len(data) * portion)
            sampled_keys = random.sample(list(data.keys()), sample_size)
            return {key: data[key] for key in sampled_keys}
        elif isinstance(data, list):
            sample_size = int(len(data) * portion)
            return random.sample(data, sample_size)
        else:
            raise ValueError("JSON file must contain a dictionary or a list.")

# Assuming the path to the JSON file is correct
path = './zc_nasbench201.json'
sampled = sample_json(path, 0.1)

# Save sampled data
with open('./zc_nasbench201_20p.json', 'w') as outfile:
    json.dump(sampled, outfile, indent=4)

