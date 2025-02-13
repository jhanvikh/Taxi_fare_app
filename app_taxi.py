import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load trained model
with open("taxi_fare_model.pkl", "rb") as file:
    model = pickle.load(file)

# Predefined locations with their coordinates
locations = {
    "Times Square": (40.7580, -73.9855),
    "JFK Airport": (40.6413, -73.7781),
    "Central Park": (40.7851, -73.9683),
    "Brooklyn Bridge": (40.7061, -73.9969),
    "Empire State Building": (40.7488, -73.9857),
    "Enter Manually": (None, None)  # For manual input
}

# Streamlit UI
st.title("🚖 NYC Taxi Fare Prediction")

# Sidebar for Pickup & Drop-off locations
st.sidebar.header("Select Locations")
pickup_option = st.sidebar.selectbox("Pickup Location", list(locations.keys()))
dropoff_option = st.sidebar.selectbox("Dropoff Location", list(locations.keys()))

# Automatically update lat/lon if a predefined location is chosen
pickup_lat, pickup_lon = locations[pickup_option]
dropoff_lat, dropoff_lon = locations[dropoff_option]

# If "Enter Manually" is selected, allow manual input
st.markdown("### Enter Trip Details")
col1, col2 = st.columns(2)

with col1:
    pickup_lat = st.number_input("Pickup Latitude", value=pickup_lat or 40.7128, format="%.6f")
    pickup_lon = st.number_input("Pickup Longitude", value=pickup_lon or -74.0060, format="%.6f")
with col2:
    dropoff_lat = st.number_input("Dropoff Latitude", value=dropoff_lat or 40.7306, format="%.6f")
    dropoff_lon = st.number_input("Dropoff Longitude", value=dropoff_lon or -73.9352, format="%.6f")

# Passenger count (Fixed issue: Can now increase properly)
passenger_count = st.slider("Number of Passengers", 1, 6, 1)

# Predict fare
if st.button("Predict Fare"):
    features = pd.DataFrame([{
        "pickup_longitude": pickup_lon,
        "pickup_latitude": pickup_lat,
        "dropoff_longitude": dropoff_lon,
        "dropoff_latitude": dropoff_lat,
        "passenger_count": passenger_count,
        "pickup_datetime_year": 2023,
        "pickup_datetime_month": 2,
        "pickup_datetime_day": 4,
        "pickup_datetime_weekday": 0,
        "pickup_datetime_hour": 14
    }])

    fare = model.predict(features)[0]
    st.success(f"Estimated Fare: **${fare:.2f}**")

# Fare Distribution Plot
df = pd.read_csv("train_df.csv")
