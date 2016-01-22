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
