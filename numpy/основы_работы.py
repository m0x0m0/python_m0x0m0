import numpy as np

a = np.array([1, 2, 3])
#print(a) - [1 2 3]

c = np.array([1, 2, 3], dtype='float32')
#print(c) - [1. 2. 3.]

#print(a.size) - количество элементов

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
#print(a[0, 4]) - 5

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#print(b[0, 1:4:2]) - [2 4]

c = np.array([[0, 2], [4, 6]])
c[0, 0] = 1
#print(c) -[[1 2]
#           [4 6]]

#Массив из нулей
a = np.zeros((2, 2))
print(a)
[[0. 0.]
 [0. 0.]]

a = np.zeros(2)
print(a)
[0. 0.]

#Массив из единиц
b = np.ones((4, 2, 2))
