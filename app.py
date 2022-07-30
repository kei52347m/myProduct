from flask import Flask,render_template
import csv
from annoy import AnnoyIndex
import random as rn

app = Flask(__name__) #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

@app.route('/')
def index():
   with open ('static/tabelog_complete.csv','r',encoding="utf-8") as f:
      reader=csv.reader(f)
   # print(reader)

      tabelog_list = list(reader)
   
   random_num = [rn.randint(0,1199) for i in range(100)]
   # print(random_num)

   tabelog_open = []
   for i in random_num:
      tabelog_open.append(tabelog_list[i+1])

   tabelog_data = []

   for i in tabelog_open:
      tabelog_data.append(i[:5]+eval(i[5])+eval(i[6]))

   # print(tabelog_data)
   return render_template("index.html",tabelog_data=tabelog_data)

@app.route('/similar/<num>')
def similar(num):
   with open ('static/tabelog_complete.csv','r',encoding="utf-8") as f:
      reader=csv.reader(f)
   # print(reader)

      tabelog_list = list(reader)
   
   # print(num)
   dim = 2048
   n_trees = 10
   index = AnnoyIndex(dim, 'euclidean')
   index.load('./image_features.ann')
   i = 0 # 0番目にインデックスされたベクトルで検索
   n = 10 # 10件検索結果を返す
   # index.get_nns_by_item(num, n)
   # index.get_nns_by_vector # ベクトルを検索する場合
   # print(index.get_nns_by_item(num, n))

   num_list = []
   for i in index.get_nns_by_item(int(num), n):
      num_list.append(i)
   # print(num_list)
   tabelog_open = []
   for i in num_list:
      tabelog_open.append(tabelog_list[i+1])
   # print(tabelog_open)

   tabelog_data = []

   for i in tabelog_open:
      tabelog_data.append(i[:5]+eval(i[5])+eval(i[6]))

   # print(tabelog_data)
   return render_template("index.html",tabelog_data=tabelog_data)



    
if __name__ == "__main__":
   app.run(debug=True)