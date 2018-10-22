import unittest
from Logic import Logic
from GUI import GUI


class TestLogic(unittest.TestCase):
    def setUp(self):  # 测试方法前执行
        self.logic = Logic('init.jpg')
        print('TestLogic.setUp')

    def tearDown(self):  # 测试方法后执行
        self.logic = None
        print('TestLogic.tearDown')

    def testJudge(self):  # 测试Logic类中的Judge函数
        self.logic = Logic('test_1_JPG_63x25.jpg')
        self.logic = Logic('test_2_JPG_500x350.jpg')
        self.logic = Logic('test_3_JPG_500x519.jpg')
        self.logic = Logic('test_4_JPG_280x280.jpg')
        self.logic = Logic('test_5_JPG_288x288.jpg')
        self.logic = Logic('test_6_PNG_500x439.png')
        self.logic = Logic('test_7_PNG_15x15.png')
        self.logic = Logic('test_8_PNG_121X121.png')
        self.logic = Logic('test_9_PNG_46X32.png')
        self.logic = Logic('test_9_PNG_46X32.png')
        print('testJudge')

    '''def testGUI(self):#测试
        from PyQt5.QtWidgets import QApplication
        app = QApplication([])
        self.gui = GUI()
        print('testGUI')'''


class TestGUI(unittest.TestCase):
    def setUp(self):
        from PyQt5.QtWidgets import QApplication
        self.app = QApplication([])
        print('TestGUI.setUp')

    def testGUI(self):
        self.gui = GUI()
        print('testGUI')

    def tearDown(self):
        self.gui = None
        print('TestGUI.teatDown')


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestLogic("testJudge"))
    # suite.addTest(TestLogic('testGUI'))
    suite.addTest(TestGUI("testGUI"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
