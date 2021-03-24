import numpy as np

a = np.arange(24).reshape((2, 3, 4))
# print(a)
# print(a.mean())
# print(a/a.mean())

# print(np.square(a))
b = np.sqrt(a)
# print(np.modf(a))

print(a)
print(b)
print(np.maximum(a, b))
print(a > b)
