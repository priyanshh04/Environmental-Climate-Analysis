# 🌍 Environmental & Climate Data Analysis

## 📌 Overview
This project explores historical climate patterns using a sample dataset from Global Surface Summary of the Year (GSOY).  
We focus on analyzing trends in:
- Average Temperature (TAVG)
- Precipitation (PRCP)

We conducted:
- ✅ **Data Preprocessing & Cleaning**  
- ✅ **Feature Selection & Transformation**  
- ✅ **Visualization & Trend Analysis**  
- ✅ **Interpretation of Climatic Insights**

---

## 🧹 Tasks Performed

### 📁 Data Preprocessing (Review 1)
- Removed or handled missing values
- Converted date columns to datetime format
- Selected key climate features: `TAVG`, `TMAX`, `TMIN`, `PRCP`
- Applied normalization using `MinMaxScaler`

### 📊 Data Visualization & Interpretation (Review 2)
This project generates six PNG charts to explore climate data
- **Correlation heatmap:**  
  Shows relationships between temperature and precipitation variables.
- **Trend charts:**  
  - **🌡️ Average Temperature (`TAVG`):** Yearly trends of average temperature.
  - **🌧️ Precipitation (`PRCP`):** Yearly trends of precipitation.
- **Temperature range chart:**  
  Visualizes the difference between maximum and minimum temperatures over time.
- **Interactive-style charts (as PNG):**  
  - Line chart of temperature over time.
  - Scatter plot of temperature vs. precipitation.

These visualizations use Seaborn and Plotly Express to highlight trends and relationships, providing clear insights through visual storytelling.

- Interpretations based on visual storytelling

---

## 📈 Visual Outputs
All visualizations are automatically saved to the `visuals/` folder:
- `correlation_heatmap.png`  
- `temperature_trend.png`  
- `precipitation_trend.png`
- `interactive_temp_trend.png`
- `scatter_temp_vs_prcp.png`
- `tmax_tmin_range.png`

## 📁 Folder Structure
```
Environmental-Climate-Analysis/
├── data/
│   └── GSOY_sample.csv
├── visuals/
│   ├── correlation_heatmap.png
│   ├── temperature_trend.png
│   ├── precipitation_trend.png
│   ├── tmax_tmin_range.png
│   ├── interactive_temp_trend.png
│   └── scatter_temp_vs_prcp.png
├── envo_analysis.py
├── Environmental & Climate Data Analysis.pptx
├── requirements.txt
└── README.md
```


## ⚙️ How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Verify the Folder Structure:
```
project-folder/
├── envo_analysis.py
├── data/
│   └── GSOY_sample.csv
├── visuals/
```

3. Run the Script:
```
python envo_analysis.py
```

Visualizations will be saved in the **`visuals/`** folder and summary statistics will be printed in the console.


## 🧠 Summary Statistics Output
The script displays basic summary statistics for selected features (**`TAVG`**, **`TMAX`**, **`TMIN`**, **`PRCP`**) after normalization.


## 💡 Insights & Storytelling
📉 Temperature Trends: Line graph reveals long-term shifts in annual average temperature.

🌧️ Precipitation Patterns: Bar chart shows yearly variation in rainfall patterns.

🔗 Variable Relationships: Correlation heatmap shows how closely different climate metrics are related.




## 🛠️ Requirements
See **`requirements.txt`** file or install directly:
```
pip install pandas==2.2.3 numpy==1.26.4 matplotlib==3.10.3 seaborn==0.13.2 scikit-learn==1.6.1 plotly==6.0.1 kaleido==0.2.1
```


## 📌 Notes
Ensure the dataset file is named **`GSOY_sample.csv`** and placed inside the **`data/`** folder.

All outputs (charts) are saved in the **`visuals/`** folder automatically.


## 📚 License
This project is submitted as part of the academic curriculum and is for educational purposes only.
