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

### 🛠️ Tech Stack

- **Frontend/UI:** Streamlit
- **ML Model:** XGBoost (`taxi_fare_model.pkl`)
- **Location Lookup:** Geopy (Nominatim API)
- **Mapping:** Folium, Streamlit-Folium
- **Other Tools:** Pandas, Datetime, Pickle

---

### 📂 Project Structure

```
├── app.py                   # Streamlit UI for user interaction and fare prediction  
├── model_training.py        # XGBoost model training and serialization script  
├── taxi_fare_model.pkl      # Trained XGBoost model (pickled)  
├── train_df.csv             # Cleaned training dataset  
└── README.md                # Project documentation  
```

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
[LinkedIn](linkedin.com/in/jhanvi-khandelwal-6535a6189)
[GitHub](github.com/jhanvikh)

---

### 📄 License

This project is open-source and available under the [MIT License](LICENSE).
