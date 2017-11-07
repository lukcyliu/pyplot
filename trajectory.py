import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
trajPath = "C:/Users/lukcy/Desktop/惯导测试数据/0828跑车/8.28滑动滤波输出.csv"

pwd = os.getcwd()
os.chdir(os.path.dirname(trajPath))
trainData = pd.read_csv(os.path.basename(trajPath))
os.chdir(pwd)



