import requests

# Define the API endpoint
url = "http://127.0.0.1:5000/predict"

# JSON payload matching the expected input features
data = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "ocean_proximity_INLAND": 0,
    "ocean_proximity_ISLAND": 0,
    "ocean_proximity_NEAR BAY": 1,
    "ocean_proximity_NEAR OCEAN": 0
}

# Make the POST request
response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    print("Prediction Response:", response.json())
else:
    print(f"Failed to get a response: {response.status_code}, {response.text}")
