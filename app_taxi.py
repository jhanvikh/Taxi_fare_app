import streamlit as st
import pickle
import pandas as pd
from geopy.geocoders import Nominatim
from datetime import datetime
import folium
from streamlit_folium import folium_static
import random

with open("taxi_fare_model.pkl", "rb") as file:
    model = pickle.load(file)

geolocator = Nominatim(user_agent="taxi_fare_app")

def get_coordinates(location_name):
    location = geolocator.geocode(location_name)
    return (location.latitude, location.longitude) if location else (None, None)

fun_facts = [
    "🚖 NYC yellow taxis have been operating since 1907!",
    "🌆 There are around 13,000 yellow cabs in NYC.",
    "🗽 A standard NYC taxi ride starts at $2.50 base fare.",
    "🚦 Taxis in NYC complete about 485,000 rides daily.",
    "💳 NYC taxis have been accepting credit cards since 2008!"
]

st.set_page_config(page_title="NYC Taxi Fare Prediction", page_icon="🚖", layout="wide")

st.markdown("""
    <style>
    .title { text-align: center; font-size: 42px; font-weight: bold; color: white; margin-bottom: 10px; }
    .input-container { background-color: rgba(255, 255, 255, 0.1); padding: 25px; border-radius: 15px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3); text-align: center; }
    .stButton>button { background-color: #ffcc00; color: black; font-weight: bold; padding: 12px 24px; border-radius: 12px; border: none; display: block; margin: auto; }
    .stButton>button:hover { background-color: #ffa500; }
    .result-container { background-color: #e9f7ef; padding: 15px; border-radius: 12px; text-align: center; font-size: 22px; font-weight: bold; color: #2d7a46; margin-top: 15px; }
    .fact { text-align: center; font-size: 16px; color: #dcdcdc; font-style: italic; margin-top: 20px; }
    .subheader { text-align: center; font-size: 24px; font-weight: bold; color: #f0f0f0; margin-top: 30px; }
    .map-container { display: flex; justify-content: center; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🚖 NYC Taxi Fare Prediction</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    pickup_location = st.text_input("📍 Pickup Location (e.g., Times Square, Manhattan)")
    dropoff_location = st.text_input("📍 Dropoff Location (e.g., JFK Airport, Brooklyn)")
    col_date, col_time = st.columns(2)
    with col_date:
        date = st.date_input("🗓️ Pickup Date", value=datetime.today())
    with col_time:
        time = st.time_input("⏰ Pickup Time", value=datetime.now().time())
    passenger_count = st.slider("👥 Number of Passengers", 1, 6, 1)
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("🚀 Predict Fare"):
    if pickup_location and dropoff_location:
        pickup_lat, pickup_lon = get_coordinates(pickup_location)
        dropoff_lat, dropoff_lon = get_coordinates(dropoff_location)

        if None in [pickup_lat, pickup_lon, dropoff_lat, dropoff_lon]:
            st.error("❌ Could not find coordinates for the provided locations.")
        else:
            pickup_datetime = datetime.combine(date, time)
            features = pd.DataFrame([{
                "pickup_longitude": pickup_lon,
                "pickup_latitude": pickup_lat,
                "dropoff_longitude": dropoff_lon,
                "dropoff_latitude": dropoff_lat,
                "passenger_count": passenger_count,
                "pickup_datetime_year": pickup_datetime.year,
                "pickup_datetime_month": pickup_datetime.month,
                "pickup_datetime_day": pickup_datetime.day,
                "pickup_datetime_weekday": pickup_datetime.weekday(),
                "pickup_datetime_hour": pickup_datetime.hour
            }])

            fare = model.predict(features)[0]
            st.markdown(f'<div class="result-container">💵 Estimated Fare: ${fare:.2f}</div>', unsafe_allow_html=True)

            st.markdown('<div class="subheader">🗺️ Trip Route Map</div>', unsafe_allow_html=True)
            trip_map = folium.Map(location=[(pickup_lat + dropoff_lat) / 2, (pickup_lon + dropoff_lon) / 2], zoom_start=13, control_scale=True)
            folium.Marker([pickup_lat, pickup_lon], tooltip="Pickup", icon=folium.Icon(color='green')).add_to(trip_map)
            folium.Marker([dropoff_lat, dropoff_lon], tooltip="Dropoff", icon=folium.Icon(color='red')).add_to(trip_map)
            folium.PolyLine([(pickup_lat, pickup_lon), (dropoff_lat, dropoff_lon)], color="blue", weight=4).add_to(trip_map)

            st.markdown('<div class="map-container">', unsafe_allow_html=True)
            folium_static(trip_map, width=850, height=450)
            st.markdown('</div>', unsafe_allow_html=True)

            random_fact = random.choice(fun_facts)
            st.markdown(f'<div class="fact">✨ {random_fact}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter both pickup and dropoff locations.")

st.markdown('<div class="subheader">🚦 Ready for your next NYC ride? Enter details above! 🗽</div>', unsafe_allow_html=True)
