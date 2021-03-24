from matplotlib import pyplot as plt

x = range(2,26,2)
y = [15,13,14,17,20,25,26,26,27,22,18,15]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

_xtick_labels = [ i/2 for i in range(2,49)]
plt.xticks(_xtick_labels)

plt.savefig("D:\\编程学习\\Python\\Study\\study01.svg")

plt.show()
