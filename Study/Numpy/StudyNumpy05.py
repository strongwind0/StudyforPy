import numpy as np

b = np.random.randint(1, 50, (2, 3, 4))
print(b)
# np.random.shuffle(b)
# print(b)
# a = np.random.permutation(b)
# print(a)

# c = np.random.choice(b, (3, 2))
# print(c)
# c = np.random.choice(b, (3, 2), replace=False)
# print(c)
# c = np.random.choice(b, (3,2), p=b/np.sum(b))
# print(c)

# print("sum=", np.sum(b))
# print("mean\n", np.mean(b, axis=1))
# print("average\n", np.average(b, axis=1, weights=[1, 2, 3]))
# print("std=", np.std(b), ",var=", np.var(b))

# print(np.max(b))
# print(np.min(b))
# print(np.argmax(b))
# print(np.argmin(b))
# print(np.unravel_index(np.argmax(b), b.shape))
# print(np.unravel_index(np.argmin(b), b.shape))
# print(np.ptp(b))
# print(np.median(b))

print(np.gradient(b))
