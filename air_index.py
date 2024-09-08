import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load the dataset
data = pd.read_csv('city_day.csv')
print("Initial data loaded from 'city_day.csv'.")

# Data Cleaning
print("\nData Cleaning Process:")

# 1. Remove duplicate rows
initial_row_count = data.shape[0]
data = data.drop_duplicates()
duplicates_removed = initial_row_count - data.shape[0]
print(f"  - Removed {duplicates_removed} duplicate rows.")

# 2. Convert 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
print("  - Converted 'Date' column to datetime format.")

# 3. Fill missing values with column means
missing_values_before = data.isnull().sum().sum()
data = data.fillna(data.mean(numeric_only=True))
missing_values_after = data.isnull().sum().sum()
filled_missing_values = missing_values_before - missing_values_after
print(f"  - Filled {filled_missing_values} missing values with column means.")

# Display the first 10 rows of the cleaned data
print(data.head(10))

# Display the last 10 rows of the cleaned data
print(data.tail(10))

# List all available cities
cities = data['City'].unique()
print("\nAvailable cities in the dataset:")
for i, city in enumerate(cities):
    print(f"{i+1}. {city}")

# Get user input for city selection
selected_city_index = int(input("\nEnter the number corresponding to the city you want to see data for: ")) - 1
selected_city = cities[selected_city_index]
print(f"\nYou selected: {selected_city}")

# Filter the data for the selected city
city_data = data[data['City'] == selected_city]

# Prepare features and target
# We'll use all columns except 'City', 'Date', and 'AQI_Bucket' as features
features = city_data.drop(['City', 'Date', 'AQI', 'AQI_Bucket'], axis=1)
target = city_data['AQI']

# Handle any remaining missing values by filling with column means
features = features.fillna(features.mean())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print(f"\nModel Performance for {selected_city}:")
print(f"  - Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"  - R-squared (R2): {r2:.2f}")

# Display accuracy as a single message
accuracy = 100 - (np.abs(y_test.iloc[0] - y_pred[0]) / y_test.iloc[0] * 100)
print(f"\nAccuracy: {accuracy:.2f}%")

# Provide a reason for the accuracy result
if accuracy > 90:
    reason = "High accuracy due to consistent data patterns and low variance in AQI levels for the selected city."
elif 70 < accuracy <= 90:
    reason = "Moderate accuracy due to some variability in the AQI data or minor inconsistencies."
else:
    reason = "Lower accuracy likely caused by high variance or missing data affecting model predictions."

print(f"Reason for Accuracy: {reason}")

# Predict AQI for a new input (for simplicity, we use the first row of the test set)
new_input = X_test.iloc[0].values.reshape(1, -1)
predicted_aqi = model.predict(new_input)[0]
print(f"\nPredicted AQI for a sample input from {selected_city}: {predicted_aqi:.2f}")

# Determine the air quality category based on predicted AQI
if predicted_aqi <= 50:
    air_quality = "Good"
elif predicted_aqi <= 100:
    air_quality = "Moderate"
elif predicted_aqi <= 150:
    air_quality = "Unhealthy for Sensitive Groups"
elif predicted_aqi <= 200:
    air_quality = "Unhealthy"
elif predicted_aqi <= 300:
    air_quality = "Very Unhealthy"
else:
    air_quality = "Hazardous"

print(f"Air Quality Category: {air_quality}")