import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the JSON data
path = 'data/processed_zc_nasbench201_layerwise.json'
with open(path, 'r') as file:
    data = json.load(file)["cifar10"]

# List of Zero-Cost measures
zcname_list = ["fisher_layerwise", "grad_norm_layerwise", "grasp_layerwise", "l2_norm_layerwise",
               "plain_layerwise", "snip_layerwise", "synflow_layerwise"]

# Function to calculate correlation matrix for a given item
def calculate_correlation_matrix(item):
    N = len(zcname_list)
    matrix = np.zeros((N, N))

    for i, zc1 in enumerate(zcname_list):
        for j, zc2 in enumerate(zcname_list):
            if i <= j:  # Fill upper triangle, as the matrix is symmetric
                corr = np.corrcoef(item[zc1], item[zc2])[0, 1]
                matrix[i, j] = corr
                matrix[j, i] = corr
    return matrix

# save to json 
save_path = "./data/arch_wise_corr_matrix.json"
save_data = {}

# process the first 100 architectures
for i in range(100):
    item = data[str(i)]
    corr_matrix = calculate_correlation_matrix(item)
    save_data[str(i)] = corr_matrix.tolist()

# save to json
with open(save_path, 'w') as file:
    json.dump(save_data, file, indent=4)

# Select the first item in the dataset to visualize its correlation matrix
first_item = list(data.values())[0]
corr_matrix = calculate_correlation_matrix(first_item)

# Plotting the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, xticklabels=zcname_list, yticklabels=zcname_list, cmap='coolwarm')
plt.title('Correlation Matrix of Layerwise Zero-Cost Scores for the First Item')
plt.show()
