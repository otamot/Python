# kmeans
k-meansによってクラスタリングを行う。
ここではN次元のベクトルを持つ各ユーザをn個のクラスタに分ける。

## 入力ファイル
inputファイルはCSVの形式で、各行に
```
label,要素1,要素2,...,要素N
```
の形式でデータが格納されている。
以下がinputファイルのsampleである。

```
user1,80,85,100
user2,96,100,100
user3,54,83,98
user4,80,98,98
user5,90,92,91
user6,84,78,82
user7,79,100,96
user8,88,92,92
user9,98,73,72
user10,75,84,85
user11,92,100,96
user12,96,92,90
user13,99,76,91
user14,75,82,88
user15,90,94,94
user16,54,84,87
user17,92,89,62
user18,88,94,97
user19,42,99,80
user20,70,98,70
user21,94,78,83
user22,52,73,87
user23,94,88,72
user24,70,73,80
user25,95,84,90
user26,95,88,84
user27,75,97,89
user28,49,81,86
user29,83,72,80
user30,75,73,88
user31,79,82,76
user32,100,77,89
user33,88,63,79
user34,100,50,86
user35,55,96,84
user36,92,74,77
user37,97,50,73
```

## 出力ファイル
出力ファイルは以下のCSV形式で出力される

```
label,cluster番号
```

sampleの入力ファイルでクラスタ数を3に指定した時の出力ファイルの例は以下の通りである。

```
user1,2
user2,2
user3,0
user4,2
user5,2
user6,1
user7,2
user8,2
user9,1
user10,2
user11,2
user12,2
user13,1
user14,2
user15,2
user16,0
user17,1
user18,2
user19,0
user20,0
user21,1
user22,0
user23,1
user24,1
user25,2
user26,2
user27,2
user28,0
user29,1
user30,1
user31,1
user32,1
user33,1
user34,1
user35,0
user36,1
user37,1

```

## コード
``` Python
# _*_ coding: utf-8 _*_
from sklearn.cluster import KMeans
import numpy as np
import sys

# kmeans()メソッド
# params
# inputTxt:入力ファイル名
# outputTxt:出力ファイル名
# nCluster:分けるクラスタの数 

# 入力のファイル形式
# CSV形式で1つめの要素はlabel,2つ目以降が各次元の数値
# label0,elm0_0,elm0_1,elm0_2,...,elm0_N
# label1,elm1_0,elm1_1,elm1_2,...,elm1_N
# ...
# labalM,elmM_0,elmM_1,elmM_2,...,elmM_N
# のような形式である。

# 出力のファイル形式
# ','区切りでもとのlabel名とcluster番号が1行ずつ書き込まれる

def kmeans(inputFile,outputFile,nCluster):
	strFeatures = []
	labels = []

	#データ入力ブロック
	#入力ファイルのオープン
	inputTxt = open(inputFile,"r")
	for line in inputTxt:
		strFeature = line[:-1].split(",")[1:]
		strFeatures.append(strFeature)
		labels.append(line.split(",")[0])
	#入力ファイルのクローズ
	inputTxt.close()


	#データ変換、kmeans実行ブロック
	#strのListからintのListに変換
	intList = [[int(elment) for elment in feature]for feature in strFeatures]
	#intのListをnumPyの配列に変換
	features = np.array(intList)
	#kmeansを実行
	kmeans_model = KMeans(n_clusters=nCluster,random_state=10).fit(features)
	#kmeansの実行によって振り分けられたクラスタをListで取得。
	clusterNumbers = kmeans_model.labels_


	#データ出力ブロック
	#出力ファイルのオープン
	outputTxt = open(outputFile,"w")
	#zip関数:複数のシーケンスオブジェクトを同時にループできる。
	for clusterNumber,label in zip(clusterNumbers,labels):
		outputTxt.write(str(label) + "," + str(clusterNumber) +"\n")
	#出力ファイルのクローズ
	outputTxt.close()


if __name__ == "__main__":
	sys.stdout.write("input file:")
	inputFile = raw_input()
	sys.stdout.write("output file:")
	outputFile = raw_input()
	sys.stdout.write("cluster_n:")
	cluster_n = int(raw_input())
	kmeans(inputFile,outputFile,cluster_n)
```

function kmeansは3つの引数をとる。
* inputFile 入力ファイルのpath
* outputFile 出力ファイルのpath
* nCluster 分けるクラスタの数


## sklearn.cluster.kmeansについて

sklearn.cluster.kmeansは以下の様な構成のライブラリである。
```python
class sklearn.cluster.KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)
```

|引数|意味|  
|:-|:-|  
|n_cluster|クラスタの数、デフォルトが8|  
|init|初期値の決め方。'kmeans++'と'random'がある。デフォルトは'kmeans++'| 

|ここに|項目を|入れます|
|:-|-:|:-:|
|ここから|テキストを|入れていきます|
|昨日|今日|明日|
|ボールペン|シャープペン|万年筆|
|iPhone|iPad|MacBook|
|テキストがながーくなっても|大丈夫なように出来ているので|レスポンシブでも安心|
