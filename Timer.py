from Logic import *
from time import sleep
from PIL import Image
import numpy as np


def loadImage():
    # 读取图片
    im = Image.open('lena.jpg')
    # 显示图片
    #     im.show()
    im = im.resize((60, 60), Image.ANTIALIAS)
    width, height = im.size
    im = im.convert("L")
    data = im.getdata()
    data = np.matrix(data, dtype='float') / 255.0
    # new_data = np.reshape(data,(width,height))
    new_data = np.reshape(data, (height, width))
    # print(new_data)


#     new_im = Image.fromarray(new_data)
#     # 显示图片
#     new_im.show()
loadImage()