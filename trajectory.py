import matplotlib.pyplot as plt
import pandas as pd
import os
trajPath = "C:/Users/lukcy/CLionProjects/GPS_INS_C/cmake-build-debug/"
file = "8.28离线结果.csv"
trainData = pd.read_csv(open(trajPath+file))
fig = plt.figure(1)
plt.scatter(trainData.ix[:,22],trainData.ix[:,23],color = "r",marker= ".",label = 'offlineTest',linewidths=1)
plt.legend()
plt.show()




