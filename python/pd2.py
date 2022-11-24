import pandas as pd

path = 'https://github.com/dongupak/DataML/raw/main/csv/'
weather_file = path + 'weather.csv'

weather = pd.read_csv(weather_file, index_col = 0, encoding='CP949')

print(weather.head(3))
print('weather 데이터의 shape :', weather.shape)