import numpy as np

# a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# b = a[2]
# c = a[1:6:2]
# print(b, c)

a = np.arange(24).reshape((2, 3, 4))
# print(a)
# print(a[1, 2, 3], a[0, 1, 3], a[-1, -2, -3])
# print(a[:, :, 1::2])
print(a-a.mean())