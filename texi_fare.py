import pandas as pd
import xgboost as xgb
import pickle

# Load dataset
df = pd.read_csv("train_df.csv")

# Convert pickup_datetime to datetime format
df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"], errors='coerce')

# Drop rows with missing pickup_datetime
df = df.dropna(subset=["pickup_datetime"])

# Extract date features
df["pickup_datetime_year"] = df["pickup_datetime"].dt.year
df["pickup_datetime_month"] = df["pickup_datetime"].dt.month
df["pickup_datetime_day"] = df["pickup_datetime"].dt.day
df["pickup_datetime_weekday"] = df["pickup_datetime"].dt.weekday
df["pickup_datetime_hour"] = df["pickup_datetime"].dt.hour

# Drop original datetime column
df.drop(columns=["pickup_datetime"], inplace=True)

# Define input features & target variable
input_cols = [
    "pickup_longitude", "pickup_latitude", 
    "dropoff_longitude", "dropoff_latitude", 
    "passenger_count", "pickup_datetime_year", 
    "pickup_datetime_month", "pickup_datetime_day",
    "pickup_datetime_weekday", "pickup_datetime_hour"
]
target_col = "fare_amount"

X = df[input_cols]
y = df[target_col]

# Train XGBoost model
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42)
model.fit(X, y)

# Save trained model using pickle
with open("taxi_fare_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("✅ Model training complete. Saved as 'taxi_fare_model.pkl'.")
