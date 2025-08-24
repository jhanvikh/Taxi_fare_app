# 🚖 MapMyFare NYC – Taxi Fare Prediction Web App

**MapMyFare NYC** is an interactive web app that predicts taxi fares in New York City based on user-provided trip details such as pickup/dropoff locations, date, time, and passenger count. It also visualizes the route on a live map and shares fun NYC taxi facts!

### 🌐 Live Features

- 📍 Accepts any NYC pickup and dropoff location names (e.g., Times Square, JFK Airport)
- 📆 Select date and time of your ride to get accurate time-based fare estimates
- 👥 Choose number of passengers (1–6)
- 🧠 Predicts fare using a trained **XGBoost** regression model
- 🗺️ Displays trip route on an interactive **Folium** map
- ✨ Shows fun NYC taxi facts on every prediction

---
### Real Time Demonstrations

<img width="1918" height="850" alt="Taxi 11" src="https://github.com/user-attachments/assets/6965ff77-e22f-44ec-ba35-2fbdb3db07cb" />

<img width="1918" height="856" alt="Taxi 22" src="https://github.com/user-attachments/assets/46b5727c-c215-4612-8498-8cadd0234d0a" />

---

### 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **ML Model:** XGBoost (`taxi_fare_model.pkl`)
- **Location Lookup:** Geopy (Nominatim API)
- **Mapping:** Folium, Streamlit-Folium
- **Other Tools:** Pandas, Datetime, Pickle

---

### 📂 Project Structure

```
├── app.py                                   # Streamlit UI for user interaction and fare prediction  
├── model_training.py                        # XGBoost model training and serialization script  
├── taxi_fare_model.pkl                      # Trained XGBoost model (pickled)  
├── train_df.csv                             # Cleaned training dataset  
├── Taxi_Fare_Prediction_project.ipynb       # Data Analysis And Processing
└── README.md                                # Project documentation  
```

---

## 💼 Business Problem & Solution

### 1. Uncertainty in Taxi Fares
- **Problem:** NYC passengers face unpredictable fares due to traffic, distance, and time of day.  
- **Solution:** MapMyFare provides transparent, ML-driven fare predictions in advance.  

### 2. Better Financial Planning for Riders & Tourists
- **Problem:** Tourists and business travelers struggle to budget for transportation.  
- **Solution:** Instant estimates help users plan their expenses before booking a ride.  

### 3. Driver & Fleet Optimization
- **Problem:** Drivers and taxi companies lack insights into profitable routes and timings.  
- **Solution:** Fare predictions enable better route allocation and shift planning.  

### 4. Improved Customer Experience
- **Problem:** Traditional taxis lack fare prediction features compared to Uber/Lyft.  
- **Solution:** Bridges the gap by offering a modern, data-driven fare prediction tool.  

### 5. Scalable Insights for City Planners & Researchers
- **Problem:** Lack of accessible tools for analyzing taxi fare dynamics.  
- **Solution:** The app + dataset can be extended for traffic analysis, congestion pricing, and urban mobility research.  


---

### 🚀 How to Run the App Locally

1. **Clone the repository:**

```bash
git clone (https://github.com/jhanvikh/Taxi_fare_app.git)
cd mapmyfare-nyc
```

2. **Install required packages:**

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist, use:
```bash
pip install streamlit geopy xgboost pandas folium streamlit-folium
```

3. **Run the app:**

```bash
streamlit run app.py
```

---

### 🧠 Model Info

- Trained on cleaned NYC taxi fare dataset
- Features: pickup/dropoff coordinates, datetime elements, passenger count
- Model: `XGBoostRegressor` with tuned hyperparameters
- Performance: RMSE ≈ 3.23 on validation set

---


### 📌 Future Improvements

- Add trip distance as a model feature  
- Include live traffic/weather data for smarter fare prediction  
- Add estimated trip duration and cab availability heatmap  

---

### 👤 Author

Jhanvi Khandelwal  
[LinkedIn](https://www.linkedin.com/in/jhanvi-khandelwal-6535a6189/)
[GitHub](https://github.com/jhanvikh)


