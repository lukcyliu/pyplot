import pandas as pd
import matplotlib.pyplot as plt
dire = "C:/Users/lukcy/Desktop/1013实时后验打包/数据/北斗参考数据/OlinkStar2017-11-15 074952/"
nmeaFile1 = "BDSView_nmea1一段.txt"
nmeaFile2 = "BDSView_nmea1.txt"
AutoInsFile = "1115AutoINS实时跑车结果.csv"
gpsFile = "1115大屯路输入.csv"
saveFile = "1115北斗nmea解析数据1.csv"

AutoINS = pd.read_csv(open(dire + AutoInsFile))
gps = pd.read_csv(open(dire+gpsFile))
gpsLoc = pd.DataFrame(gps.ix[:,[14,15,19]])
for i in range(len(gpsLoc)):
    if gpsLoc.ix[i,2] == 0:
        gpsLoc.drop(i,axis=0,inplace=True)
        
traE = list()
traL = list()
with open(dire + nmeaFile1 , 'r') as f:
    with open(dire + nmeaFile2 , 'r') as f2:
        with open(dire + saveFile , 'w') as fout:
            title = 'longitude,latitude,gpsV,gpsYaw\n'
            fout.write(title)
            for line in f:
                s = line.split(',')
                if '$GNRMC' in s:
                    E = float(s[s.index('E')-1])
                    L = float(s[s.index('N')-1])
                    V = float(s[s.index('E')+1])
                    if s[s.index('E')+2] == '':
                        s[s.index('E') + 2] = 0
                    Yaw = float(s[s.index('E')+2])
                    E = int(E / 100) + E % 100 / 60
                    L = int(L / 100) + L % 100 / 60
                    if E < 117 and L < 50:
                        out =str(E) + "," + str(L) + ","+ str(V) + "," + str(Yaw) + "\n"
                        print(out)
                        traE.append(E)
                        traL.append(L)
                    fout.write(out)
            for line2 in f2:
                s = line2.split(',')
                if '$GNRMC' in s:
                    E = float(s[s.index('E') - 1])
                    L = float(s[s.index('N') - 1])
                    V = float(s[s.index('E') + 1])
                    if s[s.index('E')+2] == '':
                        s[s.index('E') + 2] = 0
                    Yaw = float(s[s.index('E')+2])
                    E = int(E / 100) + E % 100 / 60
                    L = int(L / 100) + L % 100 / 60
                    if E < 117 and L < 50:
                        out = str(E) + "," + str(L) + ","+ str(V) +  "," + str(Yaw) + "\n"
                        traE.append(E)
                        traL.append(L)
                    fout.write(out)

fig = plt.figure(1)
plt.scatter(AutoINS.ix[:,10],AutoINS.ix[:,11],color = "g",marker= "o",label = 'Auto-INS',linewidths=3)
plt.scatter(gpsLoc.ix[:,0],gpsLoc.ix[:,1],color = "b",marker = ".",label = 'gps',linewidths=2)
plt.scatter(traE,traL,color = "r",marker= ".",label = 'BDM1',linewidths= 1)

plt.legend()
plt.show()

