import pandas as pd

# Load the abalone dataset
url = 'abalone-1.data.csv'
column_names = ['Sex','Length','Diameter','Height','Wheight','Sweight','Vweight','Shweight','Rings']
abalone = pd.read_csv(url, names=column_names)

# Examine the Rings attribute
print(abalone['Rings'].describe())

# Choose a discretization method - e.g., equal-width binning
num_bins = 5

# Alternatively, use equal-frequency binning
abalone['Rings_binned_quantile'] = pd.qcut(abalone['Rings'], q=num_bins, labels=False)

# Display the discretized attribute
print(abalone[['Rings', 'Rings_binned_quantile']].head())

# Save the updated dataset
abalone.to_csv('abalone_discretized.csv', index=False)