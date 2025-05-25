# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# 2. Load Dataset
df = pd.read_csv("GSOY_sample.csv")  # Replace with your dataset path
print("Initial data preview:")
print(df.head())

# 3. Data Cleaning
print("\nRemoving duplicates if any...")
df.drop_duplicates(inplace=True)

# Convert 'DATE' to datetime (auto-detect format)
df['DATE'] = pd.to_datetime(df['DATE'])

# Extract year as integer column for easier plotting or grouping
df['YEAR'] = df['DATE'].dt.year

# Check data types and info
print("\nData info:")
print(df.info())

# 4. Handle Missing Values
print("\nMissing values before handling:")
print(df.isnull().sum())

# Fill missing TAVG with mean
df['TAVG'].fillna(df['TAVG'].mean(), inplace=True)

# Forward fill missing PRCP values
df['PRCP'].fillna(method='ffill', inplace=True)

print("\nMissing values after handling:")
print(df.isnull().sum())

# 5. Feature Selection & Correlation
selected_features = ['TAVG', 'TMAX', 'TMIN', 'PRCP']
corr = df[selected_features].corr()

# Plot correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# 6. Data Transformation - Normalize TAVG and PRCP
scaler = MinMaxScaler()
df[['TAVG_norm', 'PRCP_norm']] = scaler.fit_transform(df[['TAVG', 'PRCP']])

print("\nData sample after normalization:")
print(df[['DATE', 'YEAR', 'TAVG', 'TAVG_norm', 'PRCP', 'PRCP_norm']].head())

# 7. Initial Visualizations

# Average Temperature Over Years
plt.figure(figsize=(10,5))
plt.plot(df['YEAR'], df['TAVG_norm'], marker='o', linestyle='-')
plt.title("Normalized Average Temperature Over Years")
plt.xlabel("Year")
plt.ylabel("Normalized Temperature")
plt.grid(True)
plt.show()

# Annual Precipitation (normalized)
plt.figure(figsize=(10,5))
plt.bar(df['YEAR'], df['PRCP_norm'], color='skyblue')
plt.title("Normalized Annual Precipitation Over Years")
plt.xlabel("Year")
plt.ylabel("Normalized Precipitation")
plt.show()

# 8. Summary Statistics
print("\nSummary Statistics:")
print(df[selected_features].describe())

# 9. Save processed data (optional)
df.to_csv("GSOY_processed.csv", index=False)

print("\nPreprocessing and initial analysis completed.")
