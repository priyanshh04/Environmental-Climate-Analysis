import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
import os

# Create folders if they don't exist
os.makedirs("data", exist_ok=True)
os.makedirs("visuals", exist_ok=True)

# Load dataset
df = pd.read_csv("data/GSOY_sample.csv")

# Convert DATE column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')
df.dropna(subset=['DATE'], inplace=True)

# Retain useful features
features = ['DATE', 'TAVG', 'TMAX', 'TMIN', 'PRCP']
df = df[features]

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Normalize numerical features
scaler = MinMaxScaler()
df[['TAVG', 'TMAX', 'TMIN', 'PRCP']] = scaler.fit_transform(df[['TAVG', 'TMAX', 'TMIN', 'PRCP']])

# Add year column
df['Year'] = df['DATE'].dt.year

# --- STATIC VISUALIZATIONS --- #

# Correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[['TAVG', 'TMAX', 'TMIN', 'PRCP']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visuals/correlation_heatmap.png")
plt.close()

# Average temperature trend
temp_by_year = df.groupby('Year')['TAVG'].mean()
plt.figure(figsize=(10, 5))
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
plt.figure(figsize=(10, 5))
prcp_by_year.plot(kind='bar', color='skyblue')
plt.title("Average Precipitation Trend")
plt.xlabel("Year")
plt.ylabel("Normalized PRCP")
plt.tight_layout()
plt.savefig("visuals/precipitation_trend.png")
plt.close()

# TMAX vs TMIN Range area chart
plt.figure(figsize=(10, 5))
plt.fill_between(df['DATE'], df['TMAX'], df['TMIN'], color='lightcoral', alpha=0.4, label='TMAX-TMIN Range')
plt.plot(df['DATE'], df['TMAX'], color='red', label='TMAX')
plt.plot(df['DATE'], df['TMIN'], color='blue', label='TMIN')
plt.title("TMAX vs TMIN Range")
plt.xlabel("Date")
plt.ylabel("Normalized Temperature")
plt.legend()
plt.tight_layout()
plt.savefig("visuals/tmax_tmin_range.png")
plt.close()

# --- INTERACTIVE VISUALIZATIONS --- #

# Line chart for TAVG
fig_temp = px.line(df, x='DATE', y='TAVG', title='Interactive Average Temperature Over Time')
fig_temp.write_html("visuals/interactive_temp_trend.html")
fig_temp.write_image("visuals/interactive_temp_trend.png")  # Saves as PNG

# Scatter plot of TAVG vs PRCP
fig_scatter = px.scatter(
    df, x='TAVG', y='PRCP', title='TAVG vs PRCP Scatter Plot',
    labels={'TAVG': 'Normalized Avg Temp', 'PRCP': 'Normalized Precipitation'},
    color='Year', hover_data=['DATE']
)
fig_scatter.write_html("visuals/scatter_temp_vs_prcp.html")
fig_scatter.write_image("visuals/scatter_temp_vs_prcp.png")  # Saves as PNG

# --- SUMMARY --- #

print("\nSummary Statistics (Normalized Values):\n")
print(df.describe())
