import pandas as pd

# Baca dataset menggunakan pandas untuk menampilkan jumlah data dan memeriksa data awal
dataset = pd.read_csv('weather_classification_data.csv')
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
import math
probabilitas = {k: v / jumlah_data_keseluruhan for k, v in counts.items()}
entropi = -sum(p * math.log(p, 2) for p in probabilitas.values() if p > 0)

print(f"Jumlah data per kelas: {counts}")
print(f"Jumlah total data (dihitung): {jumlah_data_keseluruhan}")
print(f"Entropi H(Y): {entropi}")

