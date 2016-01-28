# -*- coding: utf-8 -*-
import pandas as pd

series = pd.Series([0,1,2,3],['A','B','C','D'])
print("series=")
print(series))
# series=
# A    0
# B    1
# C    2
# D    3
# dtype: int64

# indexが文字列の場合、その文字列で要素の指定ができる
print "series['A']=" + str(series['A'])
# series['A']=0
print "series['B']=" + str(series['D']) + "\n"
# series['B']=3

# Seriesは順序も記憶しているので、整数でも指定できる。
print "series[1]=" + str(series[1])
# series[1]=1

# 要素の代入
series[1] = 10

print series
# A     0
# B    10
# C     2
# D     3
# dtype: int64
