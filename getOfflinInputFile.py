
offlinPath = "/Users/lukCy/Desktop/raspberryData/1108测试/1/raw_data.csv"
savePath = "/Users/lukCy/Desktop/raspberryData/1108测试/1/1108走一圈测试输入.csv"
with open(offlinPath,'r') as f:
    with open(savePath,'w') as fout:
        for line in f:
            # print(line)
            s = line.split(',')
            cnt = 0
            for i in range(23):
                if float(s[i]) == 0:
                   cnt +=1
            if not (float(s[13]) == 0 and float(s[12]) == 0):
                if cnt < 7 :
                    # 原数据有时间戳
                    # sout = s[1]+","+ s[2] +","+ s[3] +","+ s[4] +","+ s[5] +","+ s[6] +","+ s[7] +","+ s[8] +","+ s[9] \
                    #        + ","+ s[18]+","+ s[19]+","+s[20]+","+s[21]+","+s[12]+","+s[13]+","+s[14]+","+s[15]+","+s[16]+","\
                    #        +s[17]+","+s[22]+"\n"
                    # 原数据无时间戳
                    sout = s[0]+","+ s[1] +","+ s[2] +","+ s[3] +","+ s[4] +","+ s[5] +","+ s[6] +","+ s[7] +","+ s[8] \
                           + ","+ s[17]+","+ s[18]+","+s[19]+","+s[20]+","+s[11]+","+s[12]+","+s[13]+","+s[14]+","+s[15]+","\
                           +s[16]+","+s[21]+"\n"
                    fout.write(sout)
        fout.close()


