dire = "C:/Users/lukcy/Desktop/1013实时后验打包/数据/树莓派跑车数据/1109Turing算法大屯路跑车/第二段/"
offlinPath = "raw_data.csv"
savePath = "1108大屯路输入二段.csv"
with open(dire + offlinPath,'r') as f:
    with open(dire + savePath,'w') as fout:
        for line in f:
            # print(line)
            s = line.split(',')
            cnt = 0
            for i in range(23):
                if float(s[i]) == 0:
                   cnt += 1
            if not float(s[21]) == 0:
                if not (float(s[12]) == 0 ):
                    if not float(s[13]) == 0:
                        if cnt < 6 :
                            # 原数据有时间戳
                            # sout = s[1]+","+ s[2] +","+ s[3] +","+ s[4] +","+ s[5] +","+ s[6] +","+ s[7] +","+ s[8] +","+ s[9] \
                            #        + ","+ s[18]+","+ s[19]+","+s[20]+","+s[21]+","+s[12]+","+s[13]+","+s[14]+","+s[15]+","+s[16]+","\
                            #        +s[17]+","+s[22]+"\n"
                            # 原数据无时间戳
                            sout = s[0]+","+ s[1] +","+ s[2] +","+ s[3] +","+ s[4] +","+ s[5] +","+ s[6] +","+ s[7] +","+ s[8] \
                                   + ","+ s[17]+","+ s[18]+","+s[19]+","+s[20]+","+s[11]+","+s[12]+","+s[13]+","+s[14]+","+s[15]+","\
                                   +s[16]+","+s[21]+"\n"
                            fout.write(sout)
            else:
                if  (float(s[12]) == 0 ):
                    if  float(s[13]) == 0:

                        if cnt < 12 :
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


