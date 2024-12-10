import unittest
import requests

class TestHousePriceAPI(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:5001/predict"
        self.valid_data = {
            "longitude": -121.56,
            "latitude": 37.75,
            "housing_median_age": 28,
            "total_rooms": 3500,
            "total_bedrooms": 700,
            "population": 2300,
            "households": 650,
            "median_income": 4.2,
            "ocean_proximity_INLAND": 1,
            "ocean_proximity_ISLAND": 0,
            "ocean_proximity_NEAR BAY": 0,
            "ocean_proximity_NEAR OCEAN": 0
        }

    def test_valid_response(self):
        response = requests.post(self.url, json=self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('predicted_price', response.json())

    def test_missing_field(self):
        incomplete_data = self.valid_data.copy()
        del incomplete_data['median_income']
        response = requests.post(self.url, json=incomplete_data)
        self.assertEqual(response.status_code, 400)  # Modify based on your API error handling

if __name__ == "__main__":
    unittest.main()
