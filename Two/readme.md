# Bike Sharing Demand Prediction  
*Capstone Project – Data Science & Machine Learning*

---

## 1. Project Background

Bike-sharing systems represent an important component of urban transportation, providing environmentally friendly mobility solutions while generating large volumes of operational data. These data record explicit information regarding rental time, duration, and usage patterns, which makes them suitable for analytical modeling and predictive studies.

This capstone project aims to analyze historical bike-sharing data and develop a machine learning model capable of predicting **hourly bike rental demand** based on temporal and weather-related features.

---

## 2. Problem Statement

Accurate prediction of bike rental demand is essential for efficient operational planning in bike-sharing systems. Without reliable demand forecasting, operators may face:
- Bike shortages during peak hours
- Inefficient redistribution of bicycles
- Suboptimal resource allocation

Therefore, the main problem addressed in this project is:

> *How can historical temporal and weather data be utilized to predict hourly bike-sharing demand accurately?*

---

## 3. Objectives

The objectives of this project are as follows:
1. To explore and understand patterns in bike-sharing usage data.
2. To identify key features influencing bike rental demand.
3. To build a baseline predictive model for demand estimation.
4. To improve model performance through appropriate machine learning methods.
5. To evaluate and compare model performance using standard regression metrics.

---

## 4. Dataset Description

The dataset used in this study is the **Bike Sharing Dataset**, which contains hourly records of bike rentals along with contextual features.

### Target Variable
- `cnt`: Total number of bike rentals (casual and registered users)

### Selected Features
- `hr`: Hour of the day (0–23)
- `season`: Seasonal indicator
- `temp`, `atemp`: Normalized temperature values
- `hum`: Normalized humidity
- `weathersit`: Weather condition category
- `holiday`, `workingday`: Calendar-based indicators

The dataset documentation is provided in the accompanying PDF file.

---

## 5. Methodology

This project follows a structured data science methodology:

1. **Business and Problem Understanding**
2. **Exploratory Data Analysis (EDA)**
3. **Data Preprocessing and Feature Engineering**
4. **Baseline Model Development**
5. **Model Training and Improvement**
6. **Model Evaluation and Comparison**
7. **Conclusion and Recommendations**

All modeling steps are implemented using reproducible pipelines to ensure methodological rigor and avoid data leakage.

---

## 6. Modeling Approach

A **baseline regression model** is initially developed to establish a reference performance level. Subsequently, an **improved machine learning model** is trained to better capture non-linear relationships and feature interactions present in the data.

Model performance is evaluated using the following metrics:
- **RMSE (Root Mean Squared Error)**
- **MAE (Mean Absolute Error)**
- **R² Score**

Comparative evaluation between baseline and trained models is used to assess performance improvement and generalization capability.

---

## 7. Results and Discussion

The experimental results indicate that the trained model outperforms the baseline model across all evaluation metrics. Temporal variables, particularly hour and season, demonstrate the strongest influence on bike rental demand. The final model exhibits stable performance on both training and testing datasets, suggesting adequate generalization and minimal overfitting.

These results confirm that machine learning approaches are effective for modeling demand patterns in bike-sharing systems.

---

## 8. Conclusion

This capstone project demonstrates that historical bike-sharing data can be effectively leveraged to predict hourly rental demand using machine learning techniques. The developed model provides improved predictive accuracy compared to the baseline approach and offers meaningful insights into the factors influencing bike usage.

The findings of this study support the applicability of data-driven approaches for operational planning in urban mobility systems.

---

## 9. Limitations and Future Work

Despite satisfactory performance, several limitations remain:
- External factors such as public events and real-time weather conditions are not included.
- The model is trained on historical data from a specific context and may require adaptation for other cities.

Future work may include:
- Advanced hyperparameter optimization
- Integration of external data sources
- Deployment of the model as a real-time prediction system

---

## 10. Repository Structure

```
├── Train_bike.ipynb        # Main analysis and modeling notebook
├── data_bike_sharing.csv   # Dataset
├── Bike Sharing.pdf        # Dataset documentation
├── README.md               # Project introduction
```

---

## 11. Tools and Technologies

- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib / Seaborn  
- Jupyter Notebook  

---

## 12. Author

**Aulia Alkana**  
Capstone Project – Data Science & Machine Learning  
