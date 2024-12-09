import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from functools import partial

# Fungsi Preprocess Data (Seperti pada kode awal)
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

# Fungsi Prediksi KNN (Seperti pada kode awal)
def euclidean_distance(p1, p2):
    return sum((p1[i] - p2[i]) ** 2 for i in range(len(p1))) ** 0.5

def knn_predict(train_data, train_labels, test_point, k):
    distances = []
    for i, point in enumerate(train_data):
        dist = euclidean_distance(point, test_point)
        distances.append((dist, train_labels[i]))
    distances.sort(key=lambda x: x[0])
    nearest_neighbors = [label for _, label in distances[:k]]
    return max(set(nearest_neighbors), key=nearest_neighbors.count)

# Fungsi untuk Load Dataset dan Preprocess
def load_dataset(file_path, target_col):
    data = pd.read_csv(file_path)
    processed_data = preprocess_data(data, target_col)
    features = processed_data.drop(columns=[target_col]).values.tolist()
    labels = processed_data[target_col].values.tolist()
    return features, labels, data

# Fungsi untuk Prediksi Input Manual
def predict_weather(entry_fields, features, labels, k, label_encoder, result_label):
    try:
        input_data = []
        for field in entry_fields:
            value = float(field.get())
            input_data.append(value)
        
        # Normalisasi input berdasarkan dataset awal
        max_vals = features.max(axis=0)
        min_vals = features.min(axis=0)
        normalized_input = [(input_data[i] - min_vals[i]) / (max_vals[i] - min_vals[i]) for i in range(len(input_data))]

        # Prediksi menggunakan KNN
        prediction = knn_predict(features, labels, normalized_input, k)

        # Decode hasil prediksi
        decoded_result = {v: k for k, v in label_encoder.items()}
        result_label.config(text=f"Prediksi Weather Type: {decoded_result[prediction]}")
    except Exception as e:
        messagebox.showerror("Error", f"Input tidak valid: {str(e)}")

# GUI Tkinter
def create_gui():
    root = tk.Tk()
    root.title("Weather Type Prediction")
    root.geometry("600x500")

    # Variabel untuk dataset dan target
    features = []
    labels = []
    label_encoder = {}
    k = 5

    # Fungsi untuk load dataset
    def load_data(entry, target_col_entry, result_label):
        nonlocal features, labels, label_encoder
        file_path = entry.get()
        target_col = target_col_entry.get()

        if not file_path or not target_col:
            messagebox.showwarning("Warning", "Mohon isi file dan target kolom!")
            return

        try:
            features, labels, original_data = load_dataset(file_path, target_col)
            label_encoder = {val: idx for idx, val in enumerate(original_data[target_col].unique())}
            result_label.config(text=f"Dataset berhasil dimuat! Kolom Target: {target_col}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal memuat dataset: {str(e)}")

    # Layout GUI
    tk.Label(root, text="Path ke File Dataset (CSV):").pack(pady=5)
    file_entry = tk.Entry(root, width=50)
    file_entry.pack(pady=5)
    tk.Button(root, text="Pilih File", command=partial(select_file, file_entry)).pack(pady=5)

    tk.Label(root, text="Nama Kolom Target:").pack(pady=5)
    target_col_entry = tk.Entry(root, width=50)
    target_col_entry.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
    result_label.pack(pady=10)
    tk.Button(root, text="Muat Dataset", command=partial(load_data, file_entry, target_col_entry, result_label)).pack(pady=5)

    tk.Label(root, text="Masukkan Nilai untuk Prediksi:").pack(pady=10)
    input_fields = []
    for col in ["Humidity", "Wind Speed", "Precipitation (%)", "Cloud Cover", 
                "Atmospheric Pressure", "UV Index", "Season", "Visibility (km)", "Location"]:
        tk.Label(root, text=col).pack()
        entry = tk.Entry(root, width=30)
        entry.pack()
        input_fields.append(entry)

    result_label_prediction = tk.Label(root, text="", font=("Arial", 12), fg="blue")
    result_label_prediction.pack(pady=20)
    tk.Button(root, text="Prediksi Weather Type", 
              command=partial(predict_weather, input_fields, features, labels, k, label_encoder, result_label_prediction)).pack(pady=10)

    root.mainloop()

# Jalankan GUI
if __name__ == '__main__':
    create_gui()
