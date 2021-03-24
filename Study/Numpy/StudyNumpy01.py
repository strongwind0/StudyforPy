import numpy as np
#
#
# def pySum():
#     a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     b = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#     c = []
#     for i in range(len(a)):
#         c.append(a[i] ** 2 + b[i] ** 3)
#     return c
#
#
# def npSum():
#     a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#     b = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])
#
#     c = a ** 2 + b ** 3
#     return c
#
#
# print(pySum())
# print(npSum())
a = np.array([[[1, 2, 3, 0], [4, 5, 6, 0]], [[1, 2, 3, 0], [4, 5, 6, 0]]])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
print(a.itemsize)
