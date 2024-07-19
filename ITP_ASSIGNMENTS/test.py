#%%
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a pandas dataframe
file_path = 'cereal.csv'  # Replace with your actual file path
cereal_data = pd.read_csv(file_path)

# Calculate correlation matrix
correlation_matrix = cereal_data.corr()

# Plotting the correlation matrix
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.matshow(correlation_matrix, cmap='viridis')

# Customize ticks
ax.set_xticks(range(len(correlation_matrix.columns)))
ax.set_yticks(range(len(correlation_matrix.columns)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha='left')
ax.set_yticklabels(correlation_matrix.columns)

# Add color bar
fig.colorbar(cax)

# Add labels and title
ax.set_xlabel('Cereal Features')
ax.set_ylabel('Cereal Features')
ax.set_title('Correlation Matrix')

plt.show()

# %%
