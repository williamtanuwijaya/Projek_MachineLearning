import pandas as pd # type: ignore
import math

# Baca dataset menggunakan pandas untuk menampilkan jumlah data dan memeriksa data awal
dataset = pd.read_csv('weather_classification_data.csv')
print(dataset)
print("Jumlah total data:", len(dataset))
# print("5 baris pertama data:\n", dataset.head())

# Fungsi untuk menghitung jumlah kelas dari file CSV
def count_classes_from_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    headers = lines[0].strip().split(',')
    weather_type_index = headers.index('Weather Type')

    counts = {
        'Rainy': 0,
        'Cloudy': 0,
        'Snowy': 0,
        'Sunny' : 0
    }

    # Mengubah iterasi menjadi baris per baris
    for line in lines[1:]:
        row = line.strip().split(',')
        if len(row) > weather_type_index:  # Pastikan indeks valid
            weather_type = row[weather_type_index].strip()  # Menghapus spasi tambahan
            if weather_type in counts:
                counts[weather_type] += 1

    return counts

# Menghitung jumlah kelas dari file
file_path = 'weather_classification_data.csv'
counts = count_classes_from_csv(file_path)

# Menghitung jumlah data keseluruhan
jumlah_data_keseluruhan = sum(counts.values())

# Menghitung probabilitas dan entropi
probabilitas = {k: v / jumlah_data_keseluruhan for k, v in counts.items()}
entropi = -sum(p * math.log(p, 2) for p in probabilitas.values() if p > 0)

print(f"Jumlah data per kelas: {counts}")
print(f"Jumlah total data (dihitung): {jumlah_data_keseluruhan}")
print(f"Entropi H(Y): {entropi}")

# Fungsi untuk mengklasifikasikan suhu
def classify_temperature(temp):
    if temp <= 12:
        return 'Sangat Dingin'
    elif 13 <= temp <= 20:
        return 'Dingin'
    elif 21 <= temp <= 27:
        return 'Normal'
    elif 28 <= temp <= 33:
        return 'Hangat'
    else:
        return 'Panas'

# Pastikan ada kolom 'Temperature' di dataset
if 'Temperature' in dataset.columns:
    dataset['Temperature Category'] = dataset['Temperature'].apply(classify_temperature)
    print(dataset[['Temperature', 'Temperature Category']].head())
else:
    print("Kolom 'Temperature' tidak ditemukan dalam dataset.")

# Fungsi untuk menghitung entropi
def calculate_entropy(probabilities):
    return -sum(p * math.log2(p) for p in probabilities if p > 0)

# Fungsi untuk menghitung Information Gain
def calculate_information_gain(dataset, target_column, feature_column):
    # Hitung entropi total untuk target column (Y)
    target_counts = dataset[target_column].value_counts(normalize=True)
    H_Y = calculate_entropy(target_counts)

    # Hitung conditional entropy H(Y|X1)
    feature_values = dataset[feature_column].unique()
    weighted_entropy = 0
    for value in feature_values:
        # Pisahkan data berdasarkan nilai feature
        subset = dataset[dataset[feature_column] == value]
        subset_size = len(subset)
        total_size = len(dataset)
        
        # Hitung entropi subset
        target_counts_subset = subset[target_column].value_counts(normalize=True)
        H_Y_given_X1 = calculate_entropy(target_counts_subset)
        
        # Tambahkan weighted entropy untuk nilai feature ini
        weighted_entropy += (subset_size / total_size) * H_Y_given_X1

    # Hitung Information Gain
    information_gain = H_Y - weighted_entropy
    return information_gain

# Tentukan kolom target dan fitur
target_column = 'Weather Type'
feature_column = 'Temperature Category'

# Hitung Information Gain
info_gain = calculate_information_gain(dataset, target_column, feature_column)
print(f"Information Gain: {info_gain}")
