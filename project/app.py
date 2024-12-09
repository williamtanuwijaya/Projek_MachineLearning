from flask import Flask, render_template, request, jsonify
import pandas as pd
import math

app = Flask(__name__)

# Preprocessing functions
def preprocess_data(data, target_col):
    normalized_data = data.copy()
    encoders = {}
    for col in normalized_data.columns:
        if col == target_col:
            unique_vals = {val: idx for idx, val in enumerate(normalized_data[col].unique())}
            encoders[col] = unique_vals
            normalized_data[col] = normalized_data[col].map(unique_vals)
        elif normalized_data[col].dtype in ['float64', 'int64']:
            min_val = normalized_data[col].min()
            max_val = normalized_data[col].max()
            normalized_data[col] = (normalized_data[col] - min_val) / (max_val - min_val)
        else:
            unique_vals = {val: idx for idx, val in enumerate(normalized_data[col].unique())}
            encoders[col] = unique_vals
            normalized_data[col] = normalized_data[col].map(unique_vals)
    return normalized_data, encoders

def euclidean_distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))

def knn_predict(train_data, train_labels, test_point, k):
    distances = []
    for i, point in enumerate(train_data):
        dist = euclidean_distance(point, test_point)
        distances.append((dist, train_labels[i]))
    distances.sort(key=lambda x: x[0])
    nearest_neighbors = [label for _, label in distances[:k]]
    return max(set(nearest_neighbors), key=nearest_neighbors.count)

# Load dataset
file_path = 'weather_classification_data.csv'
dataset = pd.read_csv(file_path)
target_col = 'Weather Type'

# Preprocess dataset
processed_data, encoders = preprocess_data(dataset, target_col)
features = processed_data.drop(columns=[target_col]).values.tolist()
labels = processed_data[target_col].values.tolist()

# Decode prediction
def decode_prediction(label, encoders, target_col):
    reverse_map = {v: k for k, v in encoders[target_col].items()}
    return reverse_map[label]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.form
        test_point = []
        for col in ['Temperature', 'Humidity', 'Wind Speed', 'Precipitation (%)',
                    'Cloud Cover', 'Atmospheric Pressure', 'UV Index', 'Season',
                    'Visibility (km)', 'Location']:
            value = input_data[col]
            if col in encoders:
                value = encoders[col].get(value, None)
                if value is None:
                    return render_template('index.html', error=f"Invalid value for {col}")
            else:
                value = float(value)
            test_point.append(value)
        
        # Normalize input
        min_vals = processed_data.min()
        max_vals = processed_data.max()
        normalized_input = [(test_point[i] - min_vals[i]) / (max_vals[i] - min_vals[i])
                             if min_vals[i] != max_vals[i] else 0 for i in range(len(test_point))]
        
        # Prediction
        k = 5
        prediction = knn_predict(features, labels, normalized_input, k)
        decoded_result = decode_prediction(prediction, encoders, target_col)
        
        # Kirim hasil ke halaman
        return render_template('index.html', result=f"Weather Type: {decoded_result}")
    except Exception as e:
        return render_template('index.html', error=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
