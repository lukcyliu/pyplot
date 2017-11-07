#coding:utf-8
import  matplotlib.pyplot as plt
import pandas as pd

dire = "C:/Users/lukcy/Desktop/1013实时后验打包/数据/1107仿真测试/"
resultFile = "8.28result覆盖Vccq减去漂移权重为0镂空2450到2590.csv"
resultFile2 = "8.28result不覆盖Vccq漂移权重0.75镂空2450到2590.csv"
refrenceFile = "8.28.csv"

res = pd.read_csv(open(dire + resultFile))
ref = pd.read_csv(open(dire + refrenceFile))
res2 = pd.read_csv(open(dire + resultFile2))
refLoc = pd.DataFrame(ref.ix[:,[14,15,19]])
for i in range(len(refLoc)):
    if refLoc.ix[i,2] == 0:
        refLoc.drop([i],inplace=True)
        print(i)
fig = plt.figure(1)
plt.scatter(res.ix[:,22],res.ix[:,23],color = "b",marker= "o",label = 'turningINS')
plt.scatter(res2.ix[:,22],res2.ix[:,23],color = "y",marker= "_",label = 'mahanyINS')
plt.scatter(refLoc.ix[:,0],refLoc.ix[:,1],color = "r",marker = ".",label = 'gps')
plt.legend()
plt.show()