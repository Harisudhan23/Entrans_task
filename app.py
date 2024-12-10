from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('house_price.pkl')

# Load data for statistics pages
data = pd.read_csv('Intern Housing Data India.csv')  # Replace with your dataset path

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/descriptive-statistics')
def descriptive_statistics():
    # Summary statistics
    summary = data.describe().to_html(classes='table table-striped', border=0)
    
    # Correlation heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
    plt.savefig('static/correlation_heatmap.png', bbox_inches='tight')
    plt.close()

    return render_template('descriptive_statistics.html', summary=summary)

@app.route('/inferential-statistics')
def inferential_statistics():
    # Create any trends or relationship plots, e.g., Income vs. House Value
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='median_income', y='median_house_value', data=data, alpha=0.5)
    plt.xlabel('Median Income')
    plt.ylabel('Median House Value')
    plt.savefig('static/income_vs_house_value.png', bbox_inches='tight')
    plt.close()

    return render_template('inferential_statistics.html')

@app.route('/prediction-tool', methods=['GET', 'POST'])
def prediction_tool():
    if request.method == 'POST':
        # Extract user inputs
        form_data = request.form
        features = [
            float(form_data.get('longitude')),
            float(form_data.get('latitude')),
            float(form_data.get('housing_median_age')),
            float(form_data.get('total_rooms')),
            float(form_data.get('total_bedrooms')),
            float(form_data.get('population')),
            float(form_data.get('households')),
            float(form_data.get('median_income')),
            int(form_data.get('ocean_proximity_INLAND', 0)),
            int(form_data.get('ocean_proximity_ISLAND', 0)),
            int(form_data.get('ocean_proximity_NEAR BAY', 0)),
            int(form_data.get('ocean_proximity_NEAR OCEAN', 0)),
        ]
        prediction = model.predict([features])[0]
        return render_template('prediction_tool.html', prediction=round(prediction, 2))
    return render_template('prediction_tool.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
