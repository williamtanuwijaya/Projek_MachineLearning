import math
import pandas as pd

# Step 1: Preprocess Data
def preprocess_data(data, target_col):
    normalized_data = data.copy()
    for col in normalized_data.columns:
        if col == target_col:
            # Encoding kolom target
            unique_vals = {val: idx for idx, val in enumerate(normalized_data[col].unique())}
            normalized_data[col] = normalized_data[col].map(unique_vals)
        elif normalized_data[col].dtype in ['float64', 'int64']:
            # Normalisasi kolom numerik
            min_val = normalized_data[col].min()
            max_val = normalized_data[col].max()
            normalized_data[col] = (normalized_data[col] - min_val) / (max_val - min_val)
        else:
            # Encoding kolom string
            unique_vals = {val: idx for idx, val in enumerate(normalized_data[col].unique())}
            normalized_data[col] = normalized_data[col].map(unique_vals)
    return normalized_data

# Step 2: Hitung Jarak Euclidean
def euclidean_distance(p1, p2):
    return math.sqrt(sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))))

# Step 3: KNN Manual
def knn_predict(train_data, train_labels, test_point, k):
    distances = []
    for i, point in enumerate(train_data):
        dist = euclidean_distance(point, test_point)
        distances.append((dist, train_labels[i]))
    distances.sort(key=lambda x: x[0])  # Urutkan berdasarkan jarak
    nearest_neighbors = [label for _, label in distances[:k]]
    prediction = max(set(nearest_neighbors), key=nearest_neighbors.count)  # Voting mayoritas
    return prediction

# Step 4: Evaluasi KNN
def evaluate_knn(train_data, train_labels, test_data, test_labels, k):
    correct = 0
    for i, test_point in enumerate(test_data):
        prediction = knn_predict(train_data, train_labels, test_point, k)
        if prediction == test_labels[i]:
            correct += 1
    return correct / len(test_data)

# Step 5: Cari K Optimal
def find_optimal_k(data, labels, max_k):
    train_data = data[:int(0.8 * len(data))]  # 80% data untuk training
    train_labels = labels[:int(0.8 * len(labels))]
    test_data = data[int(0.8 * len(data)):int(0.9 * len(data))]  # 10% data untuk testing
    test_labels = labels[int(0.8 * len(labels)):int(0.9 * len(labels))]
    
    accuracies = []
    for k in range(1, max_k + 1):
        print(f"Evaluating K={k}...")
        acc = evaluate_knn(train_data, train_labels, test_data, test_labels, k)
        accuracies.append((k, acc))
    
    optimal_k = max(accuracies, key=lambda x: x[1])  # Cari k dengan akurasi terbaik
    return optimal_k

# Step 6: Main Function
if __name__ == '__main__':
    # Path ke dataset
    file_path = 'cleaned_student_prediction_data.csv'
    data = pd.read_csv(file_path)
    target_col = 'GRADE'  # Kolom target
    
    # Preprocessing data
    processed_data = preprocess_data(data, target_col)
    features = processed_data.drop(columns=[target_col]).values.tolist()
    labels = processed_data[target_col].values.tolist()

    # Cari nilai K optimal
    optimal_k = find_optimal_k(features, labels, max_k=20)
    print(f"Nilai K optimal: {optimal_k[0]} dengan akurasi: {optimal_k[1]:.2f}")
