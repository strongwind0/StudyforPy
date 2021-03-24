import numpy as np
from PIL import Image

a = np.array(Image.open("D:\\编程学习\\Python\\Study\\可莉.png"))
print(a.shape, a.dtype)

b = [255, 255, 255] - a

im = Image.fromarray(b.astype('unit8'))
im.save("1123.jpg")

