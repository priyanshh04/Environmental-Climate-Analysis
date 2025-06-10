# 🌍 Environmental & Climate Data Analysis

## 👥 Team Members
- Sarthak Goswami  
- Priyansh Gangwar  
- Krishna Garg

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
- Correlation heatmap between climate variables
- Year-wise trend analysis of:
  - 🌡️ Average Temperature (`TAVG`)
  - 🌧️ Precipitation (`PRCP`)
- Interpretations based on visual storytelling

---

## 📈 Visual Outputs
All visualizations are automatically saved to the `visuals/` folder:
- `correlation_heatmap.png`  
- `temperature_trend.png`  
- `precipitation_trend.png`  

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
│   ├── interactive_temp_trend.html
│   ├── scatter_temp_vs_prcp.html
├── envo_analysis.py
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
pip install pandas numpy matplotlib seaborn scikit-learn
```


## 📌 Notes
Ensure the dataset file is named **`GSOY_sample.csv`** and placed inside the **`data/`** folder.

All outputs (charts) are saved in the visuals/ folder automatically.


## 📚 License
This project is submitted as part of the academic curriculum and is for educational purposes only.
