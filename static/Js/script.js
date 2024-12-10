document.getElementById('prediction-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Collect form data
    const formData = new FormData(this);
    let data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    // Convert checkbox values to booleans
    data.ocean_proximity_INLAND = data.ocean_proximity_INLAND ? true : false;
    data.ocean_proximity_ISLAND = data.ocean_proximity_ISLAND ? true : false;
    data.ocean_proximity_NEAR_BAY = data.ocean_proximity_NEAR_BAY ? true : false;
    data.ocean_proximity_NEAR_OCEAN = data.ocean_proximity_NEAR_OCEAN ? true : false;

    // Send data to the Flask API
    fetch('http://127.0.0.1:5001/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        if (data.predicted_price) {
            document.getElementById('price').innerText = `Predicted Price: $${data.predicted_price}`;
        } else {
            document.getElementById('price').innerText = `Error: ${data.error}`;
        }
    })
    .catch(error => {
        document.getElementById('price').innerText = 'Error occurred while predicting price.';
    });
});
