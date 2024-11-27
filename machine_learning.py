import pandas as pd # type: ignore
import math

dataset = pd.read_csv('weather_classification_data_clear.csv')

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

# print('Entropi ', entropi)
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

# print(i_temperature)
print(dataset.describe())

kelembapan_normal = (dataset['Humidity'] <= 60).sum()
kelembapan_lembab = (dataset['Humidity'] > 60).sum()

kelembapan_normal_rainy = ((dataset['Humidity'] <= 60) & (dataset['Weather Type'] == 'Rainy')).sum()
kelembapan_normal_sunny = ((dataset['Humidity'] <= 60) & (dataset['Weather Type'] == 'Sunny')).sum()
kelembapan_normal_cloudy = ((dataset['Humidity'] <= 60) & (dataset['Weather Type'] == 'Cloudy')).sum()
kelembapan_normal_snowy = ((dataset['Humidity'] <= 60) & (dataset['Weather Type'] == 'Snowy')).sum()

kelembapan_lembab_rainy = ((dataset['Humidity'] > 60) & (dataset['Weather Type'] == 'Rainy')).sum()
kelembapan_lembab_sunny = ((dataset['Humidity'] > 60) & (dataset['Weather Type'] == 'Sunny')).sum()
kelembapan_lembab_cloudy = ((dataset['Humidity'] > 60) & (dataset['Weather Type'] == 'Cloudy')).sum()
kelembapan_lembab_snowy = ((dataset['Humidity'] > 60) & (dataset['Weather Type'] == 'Snowy')).sum()

i_humidity = entropi -sum([
  -kelembapan_normal / jumlah_keseluruhan * (
  (kelembapan_normal_rainy/kelembapan_normal * math.log2(kelembapan_normal_rainy/kelembapan_normal)) + 
  (kelembapan_normal_sunny/kelembapan_normal * math.log2(kelembapan_normal_sunny/kelembapan_normal)) + 
  (kelembapan_normal_cloudy/kelembapan_normal * math.log2(kelembapan_normal_cloudy/kelembapan_normal))+ 
  (kelembapan_normal_snowy/kelembapan_normal * math.log2(kelembapan_normal_snowy/kelembapan_normal))),

  -kelembapan_lembab / jumlah_keseluruhan * (
  (kelembapan_lembab_rainy/kelembapan_lembab * math.log2(kelembapan_lembab_rainy/kelembapan_lembab)) + 
  (kelembapan_lembab_sunny/kelembapan_lembab * math.log2(kelembapan_lembab_sunny/kelembapan_lembab)) + 
  (kelembapan_lembab_cloudy/kelembapan_lembab * math.log2(kelembapan_lembab_cloudy/kelembapan_lembab))+ 
  (kelembapan_lembab_snowy/kelembapan_lembab * math.log2(kelembapan_lembab_snowy/kelembapan_lembab)))
])

print('HUMIDITY ', i_humidity)

windspeed_very_light = (dataset['Wind Speed'] <= 6).sum()
windspeed_light = ((dataset['Wind Speed'] > 6) & (dataset['Wind Speed'] <= 14)).sum()
windspeed_normal = ((dataset['Wind Speed'] > 14) & (dataset['Wind Speed'] <= 18)).sum()
windspeed_heavy = ((dataset['Wind Speed'] > 18) & (dataset['Wind Speed'] <= 25)).sum()
windspeed_stromy = ((dataset['Wind Speed'] > 25)).sum()

windspeed_very_light_rainy = ((dataset['Wind Speed'] <= 6) & (dataset['Weather Type'] == 'Rainy')).sum()
windspeed_very_light_sunny = ((dataset['Wind Speed'] <= 6) & (dataset['Weather Type'] == 'Sunny')).sum()
windspeed_very_light_cloudy = ((dataset['Wind Speed'] <= 6) & (dataset['Weather Type'] == 'Cloudy')).sum()
windspeed_very_light_snowy = ((dataset['Wind Speed'] <= 6) & (dataset['Weather Type'] == 'Snowy')).sum()

windspeed_light_rainy = ((dataset['Wind Speed'] > 6) & (dataset['Wind Speed'] <= 14) & (dataset['Weather Type'] == 'Rainy')).sum()
windspeed_light_sunny = ((dataset['Wind Speed'] > 6) & (dataset['Wind Speed'] <= 14) & (dataset['Weather Type'] == 'Sunny')).sum()
windspeed_light_cloudy = ((dataset['Wind Speed'] > 6) & (dataset['Wind Speed'] <= 14) & (dataset['Weather Type'] == 'Cloudy')).sum()
windspeed_light_snowy = ((dataset['Wind Speed'] > 6) & (dataset['Wind Speed'] <= 14) & (dataset['Weather Type'] == 'Snowy')).sum()

windspeed_normal_rainy = ((dataset['Wind Speed'] > 14) & (dataset['Wind Speed'] <= 18) & (dataset['Weather Type'] == 'Rainy')).sum()
windspeed_normal_sunny = ((dataset['Wind Speed'] > 14) & (dataset['Wind Speed'] <= 18) & (dataset['Weather Type'] == 'Sunny')).sum()
windspeed_normal_cloudy = ((dataset['Wind Speed'] > 14) & (dataset['Wind Speed'] <= 18) & (dataset['Weather Type'] == 'Cloudy')).sum()
windspeed_normal_snowy = ((dataset['Wind Speed'] > 14) & (dataset['Wind Speed'] <= 18) & (dataset['Weather Type'] == 'Snowy')).sum()

windspeed_heavy_rainy = ((dataset['Wind Speed'] > 18) & (dataset['Wind Speed'] <= 25) & (dataset['Weather Type'] == 'Rainy')).sum()
windspeed_heavy_sunny = ((dataset['Wind Speed'] > 18) & (dataset['Wind Speed'] <= 25) & (dataset['Weather Type'] == 'Sunny')).sum()
windspeed_heavy_cloudy = ((dataset['Wind Speed'] > 18) & (dataset['Wind Speed'] <= 25) & (dataset['Weather Type'] == 'Cloudy')).sum()
windspeed_heavy_snowy = ((dataset['Wind Speed'] > 18) & (dataset['Wind Speed'] <= 25) & (dataset['Weather Type'] == 'Snowy')).sum()

windspeed_stromy_rainy = ((dataset['Wind Speed'] > 25) & (dataset['Weather Type'] == 'Rainy')).sum()
# windspeed_stromy_sunny = ((dataset['Wind Speed'] > 25) & (dataset['Weather Type'] == 'Sunny')).sum()
# print('Wind speed stromy sunny', windspeed_stromy_sunny)
windspeed_stromy_cloudy = ((dataset['Wind Speed'] > 25) & (dataset['Weather Type'] == 'Cloudy')).sum()
windspeed_stromy_snowy = ((dataset['Wind Speed'] > 25) & (dataset['Weather Type'] == 'Snowy')).sum()

i_windspeed = entropi -sum([
  -windspeed_very_light / jumlah_keseluruhan * (
  (windspeed_very_light_rainy/windspeed_very_light * math.log2(windspeed_very_light_rainy/windspeed_very_light)) + 
  (windspeed_very_light_sunny/windspeed_very_light * math.log2(windspeed_very_light_sunny/windspeed_very_light)) + 
  (windspeed_very_light_cloudy/windspeed_very_light * math.log2(windspeed_very_light_cloudy/windspeed_very_light))+ 
  (windspeed_very_light_snowy/windspeed_very_light * math.log2(windspeed_very_light_snowy/windspeed_very_light))),

  -windspeed_light / jumlah_keseluruhan * (
  (windspeed_light_rainy/windspeed_light * math.log2(windspeed_light_rainy/windspeed_light)) + 
  (windspeed_light_sunny/windspeed_light * math.log2(windspeed_light_sunny/windspeed_light)) + 
  (windspeed_light_cloudy/windspeed_light * math.log2(windspeed_light_cloudy/windspeed_light))+ 
  (windspeed_light_snowy/windspeed_light * math.log2(windspeed_light_snowy/windspeed_light))),

  -windspeed_normal / jumlah_keseluruhan * (
  (windspeed_normal_rainy/windspeed_normal * math.log2(windspeed_normal_rainy/windspeed_normal)) + 
  (windspeed_normal_sunny/windspeed_normal * math.log2(windspeed_normal_sunny/windspeed_normal)) + 
  (windspeed_normal_cloudy/windspeed_normal * math.log2(windspeed_normal_cloudy/windspeed_normal))+ 
  (windspeed_normal_snowy/windspeed_normal * math.log2(windspeed_normal_snowy/windspeed_normal))),

  -windspeed_heavy / jumlah_keseluruhan * (
  (windspeed_heavy_rainy/windspeed_heavy * math.log2(windspeed_heavy_rainy/windspeed_heavy)) + 
  (windspeed_heavy_sunny/windspeed_heavy * math.log2(windspeed_heavy_sunny/windspeed_heavy)) + 
  (windspeed_heavy_cloudy/windspeed_heavy * math.log2(windspeed_heavy_cloudy/windspeed_heavy))+ 
  (windspeed_heavy_snowy/windspeed_heavy * math.log2(windspeed_heavy_snowy/windspeed_heavy))),

  -windspeed_stromy / jumlah_keseluruhan * (
  (windspeed_stromy_rainy/windspeed_stromy * math.log2(windspeed_stromy_rainy/windspeed_stromy)) + 
  # (windspeed_stromy_sunny/windspeed_stromy * math.log2(windspeed_stromy_sunny/windspeed_stromy)) + 
  (windspeed_stromy_cloudy/windspeed_stromy * math.log2(windspeed_stromy_cloudy/windspeed_stromy))+ 
  (windspeed_stromy_snowy/windspeed_stromy * math.log2(windspeed_stromy_snowy/windspeed_stromy)))
])

print('Wind speed ',i_windspeed)