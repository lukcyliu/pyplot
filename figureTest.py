#coding:utf-8
import  matplotlib.pyplot as plt
import pandas as pd
from  numpy import  *

# dire = "C:/Users/lukcy/Desktop/1013实时后验打包/数据/树莓派跑车数据/1109Turing算法大屯路跑车/"
# resultFile = "离线resultTurning.csv"
# resultFile2 = "离线resultMahony.csv"
# refrenceFile = "1108大屯路输入.csv"
dire = "C:/Users/lukcy/Desktop/1013实时后验打包/数据/1107仿真测试/"
resultFileTurning = "8.28离线结果Turning.csv"
resultFileMahony = "8.28离线结果mahony.csv"
resultFilGPSyaw = "8.28离线结果Mod.csv"
refrenceFile = "8.28.csv"
# refrenceFileFull = "8.28滑动滤波输入.csv"

res = pd.read_csv(open(dire + resultFileTurning))
ref = pd.read_csv(open(dire + refrenceFile))
# refFull = pd.read_csv(open(dire + refrenceFileFull))
res2 = pd.read_csv(open(dire + resultFileMahony))
res3 = pd.read_csv(open(dire + resultFilGPSyaw))
refLoc = pd.DataFrame(ref.ix[:,[14,15,19]])
# refLocFull = pd.DataFrame(refFull.ix[:,[14,15,19]])
# diffE = []
# diffL = []
print(refLoc.shape)
for i in range(len(refLoc)):
    if refLoc.ix[i,2] == 0:
        print(i,res3.ix[i,34])
        refLoc.drop(i,axis=0,inplace=True)
print(refLoc.shape)

fig = plt.figure(1)
plt.scatter(res.ix[:,22],res.ix[:,23],color = "b",marker= "o",label = 'turningINS')
plt.scatter(res2.ix[:,22],res2.ix[:,23],color = "y",marker= "^",label = 'mahanyINS')
plt.scatter(res3.ix[:,22],res3.ix[:,23],color = "g",marker= ".",label = 'gpsYawINS')
plt.scatter(refLoc.ix[:,0],refLoc.ix[:,1],color = "r",marker = ".",label = 'gps')
plt.legend()
# fig2 = plt.figure(2)
# plt.plot(diffE)
# plt.plot(diffL)
plt.show()