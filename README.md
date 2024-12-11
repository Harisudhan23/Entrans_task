# House Price Prediction System
  The House Price Prediction System is a web application that leverages machine learning to predict house prices based on various features such as location, housing median age, number of rooms, and more. The backend is powered by Flask, which serves the trained machine learning model. The frontend is built using HTML, CSS, and JavaScript, where users can input features to receive a predicted house price.

## Features

   **Descriptive Statistics Page**: Visualize data distribution and correlations.

   **Inferential Statistics Page**: Identify trends and relationship in data.

   **Prediction Page**: Input house features and predict the price. 

## Technologies Used

   * Exploratory Data Analysis:
     - Pandas
     - Matplotlib
     - Seaborn
   * Backend:
     - Flask(framework)
     - Joblib
     - Scikit-learn(model training)
   * Frontend:
     - HTML, CSS
     - JavaScript

## Installation
* Prerequisites
   Python, Jupyter Notebook
   Pip 

## Steps

### Exploratory Data Analysis
    Analyze dataset characteristics with visualizations.
### Inferential Statistics
    Conduct hypothesis testing and trend analysis.
### Predictive Modeling
    Train a house price prediction model using regression algorithms. Save the trained model as house_price.pkl.  
### UI Design
    Build three pages: Descriptive Statistics, Inferential Statistics, and Prediction Tool.Display visualizations and provide input forms for predictions.              
### Backend
    Use Flask to handle routing, serve pages, and process predictions via API. Integrate UI with the trained model. 
### Testing
    Validate API endpoints, UI functionality, and prediction accuracy with unit and integration tests.
**Run - app.py

## Usage

### Home Page
    Provides an overview of the application.
### Descriptive Statistics
    Displays visualizations for data distributions:
     - Median Income Distribution
     - Correlation Matrix
### Inferential Statistics
    Explores relationships in the dataset:
     - Scatterplot: Total Rooms vs. Total Bedrooms
     - Median Income Trends Over Housing Age     
### Prediction
    - Enter house features.
    - Predict the house price in real time.

## Demo

- Open http://127.0.0.1:5000/ in your browser after running the app.
      Run - app.py

- Navigate between pages:
      Descriptive Stats: http://127.0.0.1:5000/descriptive-stats Inferential Stats: http://127.0.0.1:5000/inferential-stats Prediction: http://127.0.0.1:5000/ 

## Screenshots

- ### Descriptive Stats page  

Screenshot 2024-12-11 175717-1.png

Screenshot 2024-12-11 175747.png
- ### Inferential Stats page

Screenshot 2024-12-11 175850.png

Screenshot 2024-12-11 175915.png
- ### Prediction page

Screenshot 2024-12-11 175941.png

## Conclusion

   The House Price Prediction System combines data analysis, statistical insights, and predictive modeling into a user-friendly interface. It enables users to explore data through visualizations, understand trends with inferential statistics, and predict housing prices using machine learning. This scalable solution bridges data science and full-stack development, offering valuable insights for shakeholders decisions.              


         




    
   