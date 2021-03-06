import numpy as np
import pandas as pd
from PIL import Image

class Logic:
    size=(80, 80)
    array = np.zeros(size)

    def __init__(self, filepath):
        im = Image.open(filepath)
        # 显示图片
        #     im.show()
        im = im.resize(self.size, Image.ANTIALIAS)
        width, height = im.size
        im = im.convert("L")
        data = im.getdata()
        data = np.matrix(data, dtype='float') / 255.0
        # new_data = np.reshape(data,(width,height))
        new_data = np.reshape(data, (height, width)).tolist()
        new_data = list(map(list, zip(*new_data)))
        # print(new_data)
        for i in range(len(new_data)):
            for j in range(len(new_data[i])):
                if new_data[i][j] <= 0.5:
                    self.array[i][j] = 1
                else:
                    self.array[i][j] = 0
    @profile
    def Judge(self):
        new_array = np.zeros(self.size)
        # print(self.array)
        x = self.array.shape[0]
        y = self.array.shape[1]
        for i in range(x):
            for j in range(y):            # 遍历矩阵中的每一个细胞
                # print(self.array[i][j])
                times = 0
                start_row = i-1
                start_column = j-1
                for index in range(9):
                    row_now = start_row + int(index / 3)
                    column_now = start_column + int(index % 3)
                    if row_now >= 0 and column_now >= 0 and row_now < x and column_now < y:
                        # print(start_row + index / 3)
                        if index == 4:
                            continue
                        if self.array[row_now][column_now] == 1:
                            times += 1
                    else:
                        continue
                    # print(times)
                if self.array[i][j] == 0:           # 死细胞
                    if times == 3:
                        new_array[i][j] = 1
                    else:
                        new_array[i][j] = 0
                elif self.array[i][j] == 1:         # 活细胞
                    if times == 2 or times == 3:
                        new_array[i][j] = 1
                    else:
                        new_array[i][j] = 0
                # print(times)
        self.array = new_array
        # print(self.array)


def start():
    static = Logic('test_1_JPG_63x25.jpg')
    static.Judge()
    print(static.array)

