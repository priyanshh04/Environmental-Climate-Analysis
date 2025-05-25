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

## 🧹 Tasks Performed
- Data Cleaning and Handling Missing Values
- Feature Selection and Normalization
- Trend Visualization (Line & Bar Charts)
- Correlation Analysis
- Summary Statistics

## 📁 Folder Structure
Environmental-Climate-Analysis/
├── data/
│ └── GSOY_sample.csv
├── visuals/
│ ├── correlation_heatmap.png
│ ├── temperature_trend.png
│ └── precipitation_trend.png
├── envo_analysis.py
├── Climate_Analysis_Presentation.pptx
├── requirements.txt
└── README.md


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
