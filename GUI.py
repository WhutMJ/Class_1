from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QAction, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal, QTimer
from PyQt5.QtGui import QPainter, QColor
import sys, random, os
from Logic import *


class GUI(QMainWindow):
    static = Logic('init.jpg')
    top_x = 5
    top_y = 23
    fileFlag = 0

    def __init__(self):
        super(GUI, self).__init__()

        self.initMenu()
        self.resize(810,800)
        self.show()

    def initMenu(self):
        self.menubar = self.menuBar()
        fileAct = QAction('选择图片', self)
        fileAct.triggered.connect(self.fileChoice)
        startAct = QAction('开始', self)
        startAct.triggered.connect(self.start)
        pauseAct = QAction('暂停', self)
        pauseAct.triggered.connect(self.pause)
        self.menubar.addAction(fileAct)
        self.menubar.addAction(startAct)
        self.menubar.addAction(pauseAct)


    def start(self):
        if self.fileFlag == 1:
            self.timer = QTimer()
            self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
            self.timer.start(1000)  # 设置计时间隔并启动
        else:
            QMessageBox.information(self, '提示', '请先选择图片', QMessageBox.Yes | QMessageBox.No)

    def pause(self):
        if self.fileFlag == 1:
            self.timer.stop()
        else:
            QMessageBox.information(self, '提示', '请先选择图片', QMessageBox.Yes | QMessageBox.No)

    def fileChoice(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件",None,"JPEG Files (*.jpg);;PixMap Files (*.png)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName)
        try:
            self.static = Logic(fileName)
            self.fileFlag = 1
        except Exception:
            print('未选择')

    def operate(self):
        self.static.Judge()
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawSquare(painter)

    def drawSquare(self, painter):
        color = QColor(0, 0, 0, 255)
        size_x = self.static.array.shape[0]
        size_y = self.static.array.shape[1]
        for i in range(size_x):
            for j in range(size_y):
                if self.static.array[i][j] == 0:
                    painter.fillRect(i * 10 + self.top_x, j * 10 + self.top_y, 10, 10, QColor(0, 0, 0, 0))
                else:
                    painter.fillRect(i * 10 + self.top_x, j * 10 + self.top_y, 10, 10, color)
        painter.setPen(color.lighter())
        for i in range(size_y + 1):
            painter.drawLine(self.top_x, i * 10 + self.top_y, size_x * 10 + self.top_x, i * 10 + self.top_y)  # 横线
        for i in range(size_x + 1):
            painter.drawLine(i * 10 + self.top_x, self.top_y, i * 10 + self.top_x, size_y * 10 + self.top_y)  # 竖线


if __name__ == '__main__':
    app = QApplication([])
    tetris = GUI()
    sys.exit(app.exec_())
