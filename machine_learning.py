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
# print('Cloud Cover')
# print(dataset['Cloud Cover'].unique())

cloud_cover_party_cloudy = (dataset['Cloud Cover'] == 'partly cloudy' ).sum()
cloud_cover_clear = (dataset['Cloud Cover'] == 'clear' ).sum()
cloud_cover_overcast = (dataset['Cloud Cover'] == 'overcast' ).sum()
cloud_cover_cloudy = (dataset['Cloud Cover'] == 'cloudy' ).sum()

cloud_cover_party_cloudy_rainy = ((dataset['Cloud Cover'] == 'partly cloudy' ) & (dataset['Weather Type'] == 'Rainy')).sum()
cloud_cover_party_cloudy_sunny = ((dataset['Cloud Cover'] == 'partly cloudy' ) & (dataset['Weather Type'] == 'Sunny')).sum()
cloud_cover_party_cloudy_cloudy = ((dataset['Cloud Cover'] == 'partly cloudy') & (dataset['Weather Type'] == 'Cloudy')).sum()
cloud_cover_party_cloudy_snowy = ((dataset['Cloud Cover'] == 'partly cloudy' ) & (dataset['Weather Type'] == 'Snowy')).sum()

# cloud_cover_clear_rainy = ((dataset['Cloud Cover'] == 'clear' ) & (dataset['Weather Type'] == 'Rainy')).sum()
# print('rainy ', cloud_cover_clear_rainy)
cloud_cover_clear_sunny = ((dataset['Cloud Cover'] == 'clear' ) & (dataset['Weather Type'] == 'Sunny')).sum()
# cloud_cover_clear_cloudy = ((dataset['Cloud Cover'] == 'clear') & (dataset['Weather Type'] == 'Cloudy')).sum()
# cloud_cover_clear_snowy = ((dataset['Cloud Cover'] == 'clear' ) & (dataset['Weather Type'] == 'Snowy')).sum()

cloud_cover_overcast_rainy = ((dataset['Cloud Cover'] == 'overcast' ) & (dataset['Weather Type'] == 'Rainy')).sum()
cloud_cover_overcast_sunny = ((dataset['Cloud Cover'] == 'overcast' ) & (dataset['Weather Type'] == 'Sunny')).sum()
cloud_cover_overcast_cloudy = ((dataset['Cloud Cover'] == 'overcast') & (dataset['Weather Type'] == 'Cloudy')).sum()
cloud_cover_overcast_snowy = ((dataset['Cloud Cover'] == 'overcast' ) & (dataset['Weather Type'] == 'Snowy')).sum()

cloud_cover_cloudy_rainy = ((dataset['Cloud Cover'] == 'cloudy' ) & (dataset['Weather Type'] == 'Rainy')).sum()
cloud_cover_cloudy_sunny = ((dataset['Cloud Cover'] == 'cloudy' ) & (dataset['Weather Type'] == 'Sunny')).sum()
cloud_cover_cloudy_cloudy = ((dataset['Cloud Cover'] == 'cloudy') & (dataset['Weather Type'] == 'Cloudy')).sum()
cloud_cover_cloudy_snowy = ((dataset['Cloud Cover'] == 'cloudy' ) & (dataset['Weather Type'] == 'Snowy')).sum()

i_cloud_cover =  entropi -sum([
  -cloud_cover_party_cloudy / jumlah_keseluruhan * (
  (cloud_cover_party_cloudy_rainy/cloud_cover_party_cloudy * math.log2(cloud_cover_party_cloudy_rainy/cloud_cover_party_cloudy)) + 
  (cloud_cover_party_cloudy_sunny/cloud_cover_party_cloudy * math.log2(cloud_cover_party_cloudy_sunny/cloud_cover_party_cloudy)) + 
  (cloud_cover_party_cloudy_cloudy/cloud_cover_party_cloudy * math.log2(cloud_cover_party_cloudy_cloudy/cloud_cover_party_cloudy))+ 
  (cloud_cover_party_cloudy_snowy/cloud_cover_party_cloudy * math.log2(cloud_cover_party_cloudy_snowy/cloud_cover_party_cloudy))),
  
  -cloud_cover_clear / jumlah_keseluruhan * (
  # (cloud_cover_clear_rainy/cloud_cover_clear * math.log2(cloud_cover_clear_rainy/cloud_cover_clear)) + 
  (cloud_cover_clear_sunny/cloud_cover_clear * math.log2(cloud_cover_clear_sunny/cloud_cover_clear))
  # (cloud_cover_clear_cloudy/cloud_cover_clear * math.log2(cloud_cover_clear_cloudy/cloud_cover_clear))+ 
  # (cloud_cover_clear_snowy/cloud_cover_clear * math.log2(cloud_cover_clear_snowy/cloud_cover_clear))
  ),
  
  -cloud_cover_overcast / jumlah_keseluruhan * (
  (cloud_cover_overcast_rainy/cloud_cover_overcast * math.log2(cloud_cover_overcast_rainy/cloud_cover_overcast)) + 
  (cloud_cover_overcast_sunny/cloud_cover_overcast * math.log2(cloud_cover_overcast_sunny/cloud_cover_overcast)) + 
  (cloud_cover_overcast_cloudy/cloud_cover_overcast * math.log2(cloud_cover_overcast_cloudy/cloud_cover_overcast))+ 
  (cloud_cover_overcast_snowy/cloud_cover_overcast * math.log2(cloud_cover_overcast_snowy/cloud_cover_overcast))),
  
  -cloud_cover_cloudy / jumlah_keseluruhan * (
  (cloud_cover_cloudy_rainy/cloud_cover_cloudy * math.log2(cloud_cover_cloudy_rainy/cloud_cover_cloudy)) + 
  (cloud_cover_cloudy_sunny/cloud_cover_cloudy * math.log2(cloud_cover_cloudy_sunny/cloud_cover_cloudy)) + 
  (cloud_cover_cloudy_cloudy/cloud_cover_cloudy * math.log2(cloud_cover_cloudy_cloudy/cloud_cover_cloudy))+ 
  (cloud_cover_cloudy_snowy/cloud_cover_cloudy * math.log2(cloud_cover_cloudy_snowy/cloud_cover_cloudy)))
])

print('Cloud Cover ', i_cloud_cover)

uv_index_low = (dataset['UV Index'] <= 2).sum()
uv_index_moderate = ((dataset['UV Index'] >= 3) & (dataset['UV Index'] <= 5)).sum()
uv_index_high = ((dataset['UV Index'] >= 6) & (dataset['UV Index'] <= 7)).sum()
uv_index_very_high = ((dataset['UV Index'] >= 8) & (dataset['UV Index'] <= 10)).sum()
uv_index_extreme = ((dataset['UV Index'] >= 11)).sum()

uv_index_low_rainy = ((dataset['UV Index'] <= 2) & (dataset['Weather Type'] == 'Rainy')).sum()
uv_index_low_sunny = ((dataset['UV Index'] <= 2) & (dataset['Weather Type'] == 'Sunny')).sum()
uv_index_low_cloudy = ((dataset['UV Index'] <= 2) & (dataset['Weather Type'] == 'Cloudy')).sum()
uv_index_low_snowy = ((dataset['UV Index'] <= 2) & (dataset['Weather Type'] == 'Snowy')).sum()

uv_index_moderate_rainy = ((dataset['UV Index'] >= 3) & (dataset['UV Index'] <= 5) & (dataset['Weather Type'] == 'Rainy')).sum()
uv_index_moderate_sunny = ((dataset['UV Index'] >= 3) & (dataset['UV Index'] <= 5) & (dataset['Weather Type'] == 'Sunny')).sum()
uv_index_moderate_cloudy = ((dataset['UV Index'] >= 3) & (dataset['UV Index'] <= 5) & (dataset['Weather Type'] == 'Cloudy')).sum()
uv_index_moderate_snowy = ((dataset['UV Index'] >= 3) & (dataset['UV Index'] <= 5) & (dataset['Weather Type'] == 'Snowy')).sum()

uv_index_high_rainy = ((dataset['UV Index'] >= 6) & (dataset['UV Index'] <= 7) & (dataset['Weather Type'] == 'Rainy')).sum()
uv_index_high_sunny = ((dataset['UV Index'] >= 6) & (dataset['UV Index'] <= 7) & (dataset['Weather Type'] == 'Sunny')).sum()
uv_index_high_cloudy = ((dataset['UV Index'] >= 6) & (dataset['UV Index'] <= 7) & (dataset['Weather Type'] == 'Cloudy')).sum()
uv_index_high_snowy = ((dataset['UV Index'] >= 6) & (dataset['UV Index'] <= 7) & (dataset['Weather Type'] == 'Snowy')).sum()

uv_index_very_high_rainy = ((dataset['UV Index'] >= 8) & (dataset['UV Index'] <= 10) & (dataset['Weather Type'] == 'Rainy')).sum()
uv_index_very_high_sunny = ((dataset['UV Index'] >= 8) & (dataset['UV Index'] <= 10) & (dataset['Weather Type'] == 'Sunny')).sum()
uv_index_very_high_cloudy = ((dataset['UV Index'] >= 8) & (dataset['UV Index'] <= 10) & (dataset['Weather Type'] == 'Cloudy')).sum()
uv_index_very_high_snowy = ((dataset['UV Index'] >= 8) & (dataset['UV Index'] <= 10) & (dataset['Weather Type'] == 'Snowy')).sum()

uv_index_extreme_rainy = ((dataset['UV Index'] >= 11) & (dataset['Weather Type'] == 'Rainy')).sum()
uv_index_extreme_sunny = ((dataset['UV Index'] >= 11) & (dataset['Weather Type'] == 'Sunny')).sum()
uv_index_extreme_cloudy = ((dataset['UV Index'] >= 11) & (dataset['Weather Type'] == 'Cloudy')).sum()
uv_index_extreme_snowy = ((dataset['UV Index'] >= 11) & (dataset['Weather Type'] == 'Snowy')).sum()

i_uv_index =  entropi -sum([
  -uv_index_low / jumlah_keseluruhan * (
  (uv_index_low_rainy/uv_index_low * math.log2(uv_index_low_rainy/uv_index_low)) + 
  (uv_index_low_sunny/uv_index_low * math.log2(uv_index_low_sunny/uv_index_low)) + 
  (uv_index_low_cloudy/uv_index_low * math.log2(uv_index_low_cloudy/uv_index_low))+ 
  (uv_index_low_snowy/uv_index_low * math.log2(uv_index_low_snowy/uv_index_low))),
  
  -uv_index_moderate / jumlah_keseluruhan * (
  (uv_index_moderate_rainy/uv_index_moderate * math.log2(uv_index_moderate_rainy/uv_index_moderate)) + 
  (uv_index_moderate_sunny/uv_index_moderate * math.log2(uv_index_moderate_sunny/uv_index_moderate))+
  (uv_index_moderate_cloudy/uv_index_moderate * math.log2(uv_index_moderate_cloudy/uv_index_moderate))+ 
  (uv_index_moderate_snowy/uv_index_moderate * math.log2(uv_index_moderate_snowy/uv_index_moderate))),
  
  -uv_index_high / jumlah_keseluruhan * (
  (uv_index_high_rainy/uv_index_high * math.log2(uv_index_high_rainy/uv_index_high)) + 
  (uv_index_high_sunny/uv_index_high * math.log2(uv_index_high_sunny/uv_index_high)) + 
  (uv_index_high_cloudy/uv_index_high * math.log2(uv_index_high_cloudy/uv_index_high))+ 
  (uv_index_high_snowy/uv_index_high * math.log2(uv_index_high_snowy/uv_index_high))),
  
  -uv_index_very_high / jumlah_keseluruhan * (
  (uv_index_very_high_rainy/uv_index_very_high * math.log2(uv_index_very_high_rainy/uv_index_very_high)) + 
  (uv_index_very_high_sunny/uv_index_very_high * math.log2(uv_index_very_high_sunny/uv_index_very_high)) + 
  (uv_index_very_high_cloudy/uv_index_very_high * math.log2(uv_index_very_high_cloudy/uv_index_very_high))+ 
  (uv_index_very_high_snowy/uv_index_very_high * math.log2(uv_index_very_high_snowy/uv_index_very_high))),
  
  -uv_index_extreme / jumlah_keseluruhan * (
  (uv_index_extreme_rainy/uv_index_extreme * math.log2(uv_index_extreme_rainy/uv_index_extreme)) + 
  (uv_index_extreme_sunny/uv_index_extreme * math.log2(uv_index_extreme_sunny/uv_index_extreme)) + 
  (uv_index_extreme_cloudy/uv_index_extreme * math.log2(uv_index_extreme_cloudy/uv_index_extreme))+ 
  (uv_index_extreme_snowy/uv_index_extreme * math.log2(uv_index_extreme_snowy/uv_index_extreme)))
])

print('UV INDEX ', i_uv_index)

# print(dataset['Visibility (km)'].unique())

visibility_light_fog = (dataset['Visibility (km)'] <= 1).sum()
visibility_thin_fog = ((dataset['Visibility (km)'] > 1) & (dataset['Visibility (km)'] <= 2)).sum()
visibility_haze = ((dataset['Visibility (km)'] > 2) & (dataset['Visibility (km)'] <= 4)).sum()
visibility_light_haze = ((dataset['Visibility (km)'] > 4) & (dataset['Visibility (km)'] <= 10)).sum()
visibility_clear = (dataset['Visibility (km)'] > 10).sum()

visibility_light_fog_rainy = ((dataset['Visibility (km)'] <= 1) & (dataset['Weather Type'] == 'Rainy')).sum()
visibility_light_fog_sunny = ((dataset['Visibility (km)'] <= 1) & (dataset['Weather Type'] == 'Sunny')).sum()
visibility_light_fog_cloudy = ((dataset['Visibility (km)'] <= 1) & (dataset['Weather Type'] == 'Cloudy')).sum()
visibility_light_fog_snowy = ((dataset['Visibility (km)'] <= 1) & (dataset['Weather Type'] == 'Snowy')).sum()

visibility_thin_fog_rainy = ((dataset['Visibility (km)'] > 1) & (dataset['Visibility (km)'] <= 2) & (dataset['Weather Type'] == 'Rainy')).sum()
visibility_thin_fog_sunny = ((dataset['Visibility (km)'] > 1) & (dataset['Visibility (km)'] <= 2) & (dataset['Weather Type'] == 'Sunny')).sum()
visibility_thin_fog_cloudy = ((dataset['Visibility (km)'] > 1) & (dataset['Visibility (km)'] <= 2) & (dataset['Weather Type'] == 'Cloudy')).sum()
visibility_thin_fog_snowy = ((dataset['Visibility (km)'] > 1) & (dataset['Visibility (km)'] <= 2) & (dataset['Weather Type'] == 'Snowy')).sum()

visibility_haze_rainy = ((dataset['Visibility (km)'] > 2) & (dataset['Visibility (km)'] <= 4) & (dataset['Weather Type'] == 'Rainy')).sum()
visibility_haze_sunny = ((dataset['Visibility (km)'] > 2) & (dataset['Visibility (km)'] <= 4) & (dataset['Weather Type'] == 'Sunny')).sum()
visibility_haze_cloudy = ((dataset['Visibility (km)'] > 2) & (dataset['Visibility (km)'] <= 4) & (dataset['Weather Type'] == 'Cloudy')).sum()
visibility_haze_snowy = ((dataset['Visibility (km)'] > 2) & (dataset['Visibility (km)'] <= 4) & (dataset['Weather Type'] == 'Snowy')).sum()

visibility_light_haze_rainy = ((dataset['Visibility (km)'] > 4) & (dataset['Visibility (km)'] <= 10) & (dataset['Weather Type'] == 'Rainy')).sum()
visibility_light_haze_sunny = ((dataset['Visibility (km)'] > 4) & (dataset['Visibility (km)'] <= 10) & (dataset['Weather Type'] == 'Sunny')).sum()
visibility_light_haze_cloudy = ((dataset['Visibility (km)'] > 4) & (dataset['Visibility (km)'] <= 10) & (dataset['Weather Type'] == 'Cloudy')).sum()
visibility_light_haze_snowy = ((dataset['Visibility (km)'] > 4) & (dataset['Visibility (km)'] <= 10) & (dataset['Weather Type'] == 'Snowy')).sum()

visibility_clear_rainy = ((dataset['Visibility (km)'] > 10) & (dataset['Weather Type'] == 'Rainy')).sum()
visibility_clear_sunny = ((dataset['Visibility (km)'] > 10) & (dataset['Weather Type'] == 'Sunny')).sum()
visibility_clear_cloudy = ((dataset['Visibility (km)'] > 10) & (dataset['Weather Type'] == 'Cloudy')).sum()
visibility_clear_snowy = ((dataset['Visibility (km)'] > 10) & (dataset['Weather Type'] == 'Snowy')).sum()

i_visibility =  entropi -sum([
  -visibility_light_fog / jumlah_keseluruhan * (
  (visibility_light_fog_rainy/visibility_light_fog * math.log2(visibility_light_fog_rainy/visibility_light_fog)) + 
  (visibility_light_fog_sunny/visibility_light_fog * math.log2(visibility_light_fog_sunny/visibility_light_fog)) + 
  (visibility_light_fog_cloudy/visibility_light_fog * math.log2(visibility_light_fog_cloudy/visibility_light_fog))+ 
  (visibility_light_fog_snowy/visibility_light_fog * math.log2(visibility_light_fog_snowy/visibility_light_fog))),
  
  -visibility_thin_fog / jumlah_keseluruhan * (
  (visibility_thin_fog_rainy/visibility_thin_fog * math.log2(visibility_thin_fog_rainy/visibility_thin_fog)) + 
  (visibility_thin_fog_sunny/visibility_thin_fog * math.log2(visibility_thin_fog_sunny/visibility_thin_fog))+
  (visibility_thin_fog_cloudy/visibility_thin_fog * math.log2(visibility_thin_fog_cloudy/visibility_thin_fog))+ 
  (visibility_thin_fog_snowy/visibility_thin_fog * math.log2(visibility_thin_fog_snowy/visibility_thin_fog))),
  
  -visibility_haze / jumlah_keseluruhan * (
  (visibility_haze_rainy/visibility_haze * math.log2(visibility_haze_rainy/visibility_haze)) + 
  (visibility_haze_sunny/visibility_haze * math.log2(visibility_haze_sunny/visibility_haze)) + 
  (visibility_haze_cloudy/visibility_haze * math.log2(visibility_haze_cloudy/visibility_haze))+ 
  (visibility_haze_snowy/visibility_haze * math.log2(visibility_haze_snowy/visibility_haze))),
  
  -visibility_light_haze / jumlah_keseluruhan * (
  (visibility_light_haze_rainy/visibility_light_haze * math.log2(visibility_light_haze_rainy/visibility_light_haze)) + 
  (visibility_light_haze_sunny/visibility_light_haze * math.log2(visibility_light_haze_sunny/visibility_light_haze)) + 
  (visibility_light_haze_cloudy/visibility_light_haze * math.log2(visibility_light_haze_cloudy/visibility_light_haze))+ 
  (visibility_light_haze_snowy/visibility_light_haze * math.log2(visibility_light_haze_snowy/visibility_light_haze))),
  
  -visibility_clear / jumlah_keseluruhan * (
  (visibility_clear_rainy/visibility_clear * math.log2(visibility_clear_rainy/visibility_clear)) + 
  (visibility_clear_sunny/visibility_clear * math.log2(visibility_clear_sunny/visibility_clear)) + 
  (visibility_clear_cloudy/visibility_clear * math.log2(visibility_clear_cloudy/visibility_clear))+ 
  (visibility_clear_snowy/visibility_clear * math.log2(visibility_clear_snowy/visibility_clear)))
])

print('Visibility ', i_visibility)