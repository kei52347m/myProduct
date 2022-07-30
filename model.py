import tensorflow as tf
import pathlib
import os
from natsort import natsorted
import numpy as np
from tensorflow.keras.preprocessing import image
import tensorflow as tf
from tensorflow.keras.applications import resnet
from annoy import AnnoyIndex

# device_name = tf.test.gpu_device_name()

# # 画像のロード
# dir_path = "./images"
# image_path_list = []

# for img_path in pathlib.Path(dir_path).glob("*.jpg"): # jpgの画像ファイルのパスをすべて取得
#     image_path_list.append(img_path) # img_path_listにパスを追加
# image_path_list = natsorted(image_path_list) # ファイル名を辞書順に並べる
# #print(image_path_list)

# # 行列形式への変換
# images = []

# for img_path in image_path_list:
#     img = image.load_img(img_path, target_size=(224, 224)) # 画像の読み込み
#     raw_image = image.img_to_array(img) # 多次元配列への変換
#     images.append(raw_image) # 変換したデータをimagesに追加
    
# images = np.array(images) # 四次元のndarrayに変換
# #images

# # ResNetの初期化
# model = tf.keras.applications.ResNet152(include_top=False,
#                                        weights='imagenet',
#                                        input_tensor=None,
#                                        pooling='avg',
#                                        classes=1000)

# # 特徴ベクトルの作成
# preprocessed = resnet.preprocess_input(images)
# features = model.predict(preprocessed)
# #print(features)

# Annoyの実装
dim = 2048
n_trees = 10

index = AnnoyIndex(dim, 'euclidean') # dim:インデックスの次元, metric:距離の種類（ユーグリット距離・コサイン類似度のときは'euclidean'）
# for i, feature in enumerate(features):
#   index.add_item(i, feature) # インデックスに順番にベクトルを追加（検索対象となるベクトルの登録）

# index.build(n_trees, n_jobs=-1) # インデックスをビルド（登録されたベクトルに対する検索を高速化するための構造の作成）
# index.save('./image_features.ann')

# モデルをロードし、実際に検索する
dim = 2048
n_trees = 10

index = AnnoyIndex(dim, 'euclidean')
index.load('./image_features.ann')
i = 0 # 0番目にインデックスされたベクトルで検索
n = 10 # 10件検索結果を返す
index.get_nns_by_item(1, n)
# index.get_nns_by_vector # ベクトルを検索する場合
print(index.get_nns_by_item(1, n))

