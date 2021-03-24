import numpy as np

a = np.arange(100).reshape(5, 10, 2)

# np.savetxt('D:\\编程学习\\Python\\Study\\a.scv', a, fmt='%d', delimiter=',')
# print("已执行保存操作")
# b = np.loadtxt('D:\\编程学习\\Python\\Study\\a.scv', dtype=np.int, delimiter=',')
# print(b)

# a.tofile('D:\\编程学习\\Python\\Study\\a.dat', sep=",", format="%d")
# print("已执行保存操作")
#
# b = np.fromfile('D:\\编程学习\\Python\\Study\\a.dat', dtype=int, count=-1, sep=",")
# print(b)
#
# a.tofile('D:\\编程学习\\Python\\Study\\a2.dat', format="%d")
# print("已执行保存操作")
#
# c = np.fromfile('D:\\编程学习\\Python\\Study\\a2.dat', dtype=int, count=-1).reshape(2, 5, 10)
# print(c)

# np.save('D:\\编程学习\\Python\\Study\\a.npy', a)
# b = np.load('D:\\编程学习\\Python\\Study\\a.npy')
# print(b)
#
# np.savez('D:\\编程学习\\Python\\Study\\a.npz', a)
# b = np.load('D:\\编程学习\\Python\\Study\\a.npz')
# print(b)
