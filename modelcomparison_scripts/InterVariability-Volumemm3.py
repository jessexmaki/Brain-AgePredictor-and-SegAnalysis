import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#update to apply dataframe from parser
concatenated_df = "dataframe"

# List of models (unique values in the 'Model' column)
#models = concatenated_df['Model'].unique()
concatenated_df['Volume_mm3'] = pd.to_numeric(concatenated_df['Volume_mm3'], errors='coerce')
concatenated_df = concatenated_df.dropna(subset=['Volume_mm3'])

concatenated_df['Model'] = concatenated_df['Model'].astype('category')

plt.figure(figsize=(10, 8))
sns.set(style='whitegrid')


sns.boxplot(x='Model', y='Volume_mm3', data=concatenated_df,sym='')

plt.title('Inter-Model Variability - Volume_mm3')
plt.xlabel('Model')
plt.ylabel('Volume_mm3')

# Set the y-axis to a logarithmic scale
plt.yscale('log')  

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()