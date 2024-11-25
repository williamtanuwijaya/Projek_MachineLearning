import pandas as pd # type: ignore
import math

dataset = pd.read_csv('weather_classification_data.csv')

weather_type_rainy = (dataset['Weather Type'] == 'Rainy').sum()
weather_type_sunny = (dataset['Weather Type'] == 'Sunny').sum()
weather_type_cloudy = (dataset['Weather Type'] == 'Cloudy').sum()
weather_type_snowy = (dataset['Weather Type'] == 'Snowy').sum()

jumlah_keseluruhan = weather_type_rainy + weather_type_sunny + weather_type_cloudy + weather_type_snowy

entropi = -sum([
  (weather_type_rainy / jumlah_keseluruhan) * math.log2(weather_type_rainy / jumlah_keseluruhan),
  (weather_type_sunny / jumlah_keseluruhan) * math.log2(weather_type_sunny / jumlah_keseluruhan),
  (weather_type_cloudy / jumlah_keseluruhan) * math.log2(weather_type_cloudy / jumlah_keseluruhan),
  (weather_type_snowy / jumlah_keseluruhan) * math.log2(weather_type_snowy / jumlah_keseluruhan),
])

# print(entropi)
print((dataset['Temperature'] < 12).sum())

sangat_dingin = (dataset['Temperature'] <= 12).sum()
dingin = ((dataset['Temperature'] > 12) & (dataset['Temperature'] <= 20)).sum()
normal = ((dataset['Temperature'] > 20) & (dataset['Temperature'] <= 27)).sum()
hangat = ((dataset['Temperature'] > 27) & (dataset['Temperature'] <= 33)).sum()
panas = (dataset['Temperature'] > 33).sum()
# print(sum([sangat_dingin, dingin, normal, hangat, panas]))
print(sangat_dingin)

sangat_dingin_rainy = ((dataset['Temperature'] <= 12) & (dataset['Weather Type'] == 'Rainy')).sum()
sangat_dingin_sunny = ((dataset['Temperature'] <= 12) & (dataset['Weather Type'] == 'Sunny')).sum()
sangat_dingin_cloudy = ((dataset['Temperature'] <= 12) & (dataset['Weather Type'] == 'Cloudy')).sum()
sangat_dingin_snowy = ((dataset['Temperature'] <= 12) & (dataset['Weather Type'] == 'Snowy')).sum()

dingin_rainy = ((dataset['Temperature'] > 12) & (dataset['Temperature'] <= 20) & (dataset['Weather Type'] == 'Rainy')).sum()
dingin_sunny = ((dataset['Temperature'] > 12) & (dataset['Temperature'] <= 20) & (dataset['Weather Type'] == 'Sunny')).sum()
dingin_cloudy = ((dataset['Temperature'] > 12) & (dataset['Temperature'] <= 20) & (dataset['Weather Type'] == 'Cloudy')).sum()
dingin_snowy = ((dataset['Temperature'] > 12) & (dataset['Temperature'] <= 20) & (dataset['Weather Type'] == 'Snowy')).sum()

normal_rainy = ((dataset['Temperature'] > 20) & (dataset['Temperature'] <= 27) & (dataset['Weather Type'] == 'Rainy')).sum()
normal_sunny = ((dataset['Temperature'] > 20) & (dataset['Temperature'] <= 27) & (dataset['Weather Type'] == 'Sunny')).sum()
normal_cloudy = ((dataset['Temperature'] > 20) & (dataset['Temperature'] <= 27) & (dataset['Weather Type'] == 'Cloudy')).sum()
normal_snowy = ((dataset['Temperature'] > 20) & (dataset['Temperature'] <= 27) & (dataset['Weather Type'] == 'Snowy')).sum()

hangat_rainy = ((dataset['Temperature'] > 27) & (dataset['Temperature'] <= 33) & (dataset['Weather Type'] == 'Rainy')).sum()
hangat_sunny = ((dataset['Temperature'] > 27) & (dataset['Temperature'] <= 33) & (dataset['Weather Type'] == 'Sunny')).sum()
hangat_cloudy = ((dataset['Temperature'] > 27) & (dataset['Temperature'] <= 33) & (dataset['Weather Type'] == 'Cloudy')).sum()
hangat_snowy = ((dataset['Temperature'] > 27) & (dataset['Temperature'] <= 33) & (dataset['Weather Type'] == 'Snowy')).sum()

panas_rainy = ((dataset['Temperature'] > 33) & (dataset['Weather Type'] == 'Rainy')).sum()
panas_sunny = ((dataset['Temperature'] > 33) & (dataset['Weather Type'] == 'Sunny')).sum()
panas_cloudy = ((dataset['Temperature'] > 33) & (dataset['Weather Type'] == 'Cloudy')).sum()
panas_snowy = ((dataset['Temperature'] > 33) & (dataset['Weather Type'] == 'Snowy')).sum()

i_temperature = entropi - sum([
  -sangat_dingin/ jumlah_keseluruhan * (
  (sangat_dingin_rainy/sangat_dingin * math.log2(sangat_dingin_rainy/sangat_dingin)) + 
  (sangat_dingin_sunny/sangat_dingin * math.log2(sangat_dingin_sunny/sangat_dingin)) + 
  (sangat_dingin_cloudy/sangat_dingin * math.log2(sangat_dingin_cloudy/sangat_dingin))+ 
  (sangat_dingin_snowy/sangat_dingin * math.log2(sangat_dingin_snowy/sangat_dingin))),

  -dingin / jumlah_keseluruhan * (
  (dingin_rainy/dingin * math.log2(dingin_rainy/dingin)) + 
  (dingin_sunny/dingin * math.log2(dingin_sunny/dingin)) + 
  (dingin_cloudy/dingin * math.log2(dingin_cloudy/dingin))+ 
  (dingin_snowy/dingin * math.log2(dingin_snowy/dingin))),

  -normal / jumlah_keseluruhan * (
  (normal_rainy/normal * math.log2(normal_rainy/normal)) + 
  (normal_sunny/normal * math.log2(normal_sunny/normal)) + 
  (normal_cloudy/normal * math.log2(normal_cloudy/normal))+ 
  (normal_snowy/normal * math.log2(normal_snowy/normal))),

  -hangat / jumlah_keseluruhan * (
  (hangat_rainy/hangat * math.log2(hangat_rainy/hangat)) + 
  (hangat_sunny/hangat * math.log2(hangat_sunny/hangat)) + 
  (hangat_cloudy/hangat * math.log2(hangat_cloudy/hangat))+ 
  (hangat_snowy/hangat * math.log2(hangat_snowy/hangat))),

  -panas / jumlah_keseluruhan * (
  (panas_rainy/panas * math.log2(panas_rainy/panas)) + 
  (panas_sunny/panas * math.log2(panas_sunny/panas)) + 
  (panas_cloudy/panas * math.log2(panas_cloudy/panas))+ 
  (panas_snowy/panas * math.log2(panas_snowy/panas)))
])

print(i_temperature)