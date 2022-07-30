import requests
import pandas as pd
import time

# urlから画像をダウンロードする関数を作成
def download_file(url, file_name):
    response = requests.get(url)
    image = response.content

    with open(file_name, "wb") as aaa:
        aaa.write(image)


df = pd.read_csv('./tabelog_complete.csv') # csvファイルの読み込み
cafe_images1 = list(df['cafe_images1']) # cafe_images1列だけを読み込んてリストにする

url_list = [] # urlを格納するリストを作成

# urlが3つずつセットになってるものから、最初の1つを取り出す
# listではなくてstr(文字列)になってたから、for文は使えない！代わりに特定の文字列までを抽出するという方法を使ってる！
# 抽出する方法は参考リンク見てみてね
for cafe_image1 in cafe_images1:
    cafe_image1.replace('""', '') # クォーテーションを削除
    # '.jpg'という文字列が出てくるまでを抽出
    target = '.jpg'
    idx = cafe_image1.find(target)
    r = cafe_image1[2:idx] + '.jpg' # 最初の2は、[' を含まないようにするため
    url_list.append(r) # 取り出したurlの文字列（r）をurl_listに追加

for i in range(len(url_list)):
    url = url_list[i]
    file_name = './images/' + '{0:04d}'.format(i) + '.jpg' #imagesフォルダに順番に保存
    download_file(url, file_name)
    print(i) #何件目までダウンロードできたか出力
    time.sleep(1) #サーバーに負荷をかけないように1秒スリープ


