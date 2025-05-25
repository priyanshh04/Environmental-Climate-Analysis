import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import MinMaxScaler

# Load Dataset
df = pd.read_csv('data/GSOY_sample.csv')

# Convert DATE column to datetime
df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
df.dropna(subset=['DATE'], inplace=True)

# Select useful features
features = ['DATE', 'TAVG', 'TMAX', 'TMIN', 'PRCP']
df = df[features]

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Normalize numeric data
scaler = MinMaxScaler()
df[['TAVG', 'TMAX', 'TMIN', 'PRCP']] = scaler.fit_transform(df[['TAVG', 'TMAX', 'TMIN', 'PRCP']])

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['TAVG', 'TMAX', 'TMIN', 'PRCP']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png")
plt.close()

# Temperature trend
df['Year'] = df['DATE'].dt.year
temp_by_year = df.groupby('Year')['TAVG'].mean()

plt.figure(figsize=(10,5))
temp_by_year.plot()
plt.title("Average Temperature Trend")
plt.xlabel("Year")
plt.ylabel("Normalized TAVG")
plt.grid(True)
plt.tight_layout()
plt.savefig("visuals/temperature_trend.png")
plt.close()

# Precipitation trend
prcp_by_year = df.groupby('Year')['PRCP'].mean()

plt.figure(figsize=(10,5))
prcp_by_year.plot(kind='bar', color='skyblue')
plt.title("Average Precipitation Trend")
plt.xlabel("Year")
plt.ylabel("Normalized PRCP")
plt.tight_layout()
plt.savefig("visuals/precipitation_trend.png")
plt.close()

# Summary statistics
print("Summary Statistics:")
print(df.describe())
