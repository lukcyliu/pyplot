import numpy as np
import matplotlib.pyplot as plt

offlinePath = "/Users/lukCy/Desktop/惯导项目/CLionProjects/实验数据/1014北邮/离线运行结果/imu_velocity_ENU.csv"
realtimePath = "/Users/lukCy/Desktop/惯导项目/CLionProjects/实验数据/1014北邮/imu_velocity_ENU.csv"

with open(offlinePath,'r') as fo , open(realtimePath,'r') as fr:
    for lineo in fo:
        so = lineo.split(',')
        voe = float(so[1])
        von = float(so[2])
        vou = float(so[3])
        plt.plot(so[0],voe)
    for liner in fr:
        sr = liner.split(',')
        vre = float(sr[0])
        vrn = float(sr[1])
        vru = float(sr[2])
        print("offV = %s readV = %s" % (so, sr))
        plt.plot(so[0],vre)
    plt.show()




