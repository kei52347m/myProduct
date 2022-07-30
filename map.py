import pandas as pd

df = pd.read_csv('./tabelog_complete.csv') # csvファイルの読み込み
cafe_adresses = list(df['cafe_adresses']) # 住所と名前を読み込んてリストにする
cafe_names = list(df['cafe_names'])


# print(len(cafe_adresses))
# print(len(cafe_names))
cafe_maps = []

#URLの定義
origin = "https://www.google.co.jp/maps/search/"

for name,adress in zip(cafe_names,cafe_adresses):
  mapURL = origin + adress + ("+") + name
  cafe_maps.append(mapURL)

