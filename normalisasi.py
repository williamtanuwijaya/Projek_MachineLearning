import pandas as pd
from scipy.stats import zscore

file_path = 'weather_classification_data.csv' 
df = pd.read_csv(file_path)

# Fungsi untuk menghapus outlier menggunakan Z-Score
def remove_outliers_zscore(df, column, threshold=3):
    z_scores = zscore(df[column])
    return df[abs(z_scores) <= threshold]

# Menghapus outlier pada kolom Humidity dan Precipitation (%)
df_clean_zscore = remove_outliers_zscore(df, "Humidity", threshold=3)
df_clean_zscore = remove_outliers_zscore(df_clean_zscore, "Precipitation (%)", threshold=3)

# Simpan data yang telah dibersihkan
df_clean_zscore.to_csv('cleaned_weather_data_zscore.csv', index=False)

# Menampilkan ukuran data sebelum dan sesudah pembersihan
print(f"Data asli: {df.shape[0]} baris")
print(f"Data setelah pembersihan outlier: {df_clean_zscore.shape[0]} baris")