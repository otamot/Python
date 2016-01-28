# -*- coding: utf-8 -*-
import pandas as pd

# ListからSeriesの生成(ラベル指定なし)
# ラベルの指定がない場合は0から始まる整数になる。(listと同様)
list_a = [10,20,30];
series_list = pd.Series(list_a)
print(series_list)
# 0    10
# 1    20
# 2    30
# dtype: int64

# ListからSeriesの生成(ラベル指定)
list_label = ['a','b','c']
series_list_label = pd.Series(list_a,list_label)
print(series_list_label)
# a    10
# b    20
# c    30
# type: int64

# dictからSeriesの生成
dict_a = {'A':1.0,'B':2.0,'C':3.0}
series_dict = pd.Series(dict_a)
print(series_dict)
# A    1
# B    2
# C    3
# dtype: float64
