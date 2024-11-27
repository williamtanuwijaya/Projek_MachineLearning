import pandas as pd

# Membaca file CSV
file_path = 'weather_classification_data.csv' 
df = pd.read_csv(file_path)

# Fungsi untuk menghapus outlier berdasarkan batas nilai
def remove_outliers_threshold(df, column, threshold=100):
    return df[df[column] <= threshold]

# Kolom yang ingin dibersihkan dari outlier
columns_to_clean = ["Humidity", "Precipitation (%)"]

# Salin data asli
df_clean = df.copy()

# Menghapus outlier pada kolom yang dipilih
for column in columns_to_clean:
    df_clean = remove_outliers_threshold(df_clean, column, threshold=100)

# Simpan data yang telah dibersihkan
df_clean.to_csv('weather_classification_data_clear.csv', index=False)

# Menampilkan ukuran data sebelum dan sesudah pembersihan
print(f"Data asli: {df.shape[0]} baris")
print(f"Data setelah pembersihan outlier: {df_clean.shape[0]} baris")
