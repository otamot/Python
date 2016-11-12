import numpy as np

A = np.array([1,2,3,4])
print(A)
# [1 2 3 4]
print(np.ndim(A))
# 1
print(A.shape)
# (4,)
print(A.shape[0])
# 4




B = np.array([[1,2],[3,4],[5,6]])
print(B)
# [[1 2]
#  [3 4]
#  [5 6]]
print(np.ndim(B))
# 2
print(B.shape)
# (3, 2)



C = np.array([[1,2], [3,4]])
print(C.shape)
# (2, 2)
D = np.array([[5,6], [7,8]])
print(D.shape)
# (2, 2)
print(np.dot(C, D))
# [[19 22]
#  [43 50]]
