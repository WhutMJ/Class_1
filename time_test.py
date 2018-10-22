from GUI import *
from Logic import *

if __name__ == "__main__":
    import cProfile

    # 直接把分析结果打印到控制台
    cProfile.run("start()")
    # 把分析结果保存到文件中,不过内容可读性差...需要调用pstats模块分析结果
    # cProfile.run("start()", "result")
