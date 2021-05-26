# -*- coding: utf-8 -*-

#  genplot.py
#
#  ~~~~~~~~~~~~
#
#  Function generate plot
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 21.05.2021
#  Last change: 24.05.2021 Li Yonghu 
#
#  Language: Python 3.7 
#  ------------------------------------------------------------------
#  GNU GPL
#  
 
#

# Module Imports
from matplotlib import pyplot as plt
#from matplotlib.font_manager import FontProperties

def genplot(datadict,mydatadict,myylabel):

   
    # 设置图片大小和分辨率
    #fig=plt.figure(figsize=(8, 6), dpi=160)

    #fig1,ax = plt.subplots(1, 1, figsize=(12, 9))

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    #font = FontProperties(fname='/System/Library/Fonts/STHeiti Light.ttc', size=16)


    datakey = list(datadict.keys())
    datalen = len(datadict[datakey[0]])#任意一组列表的大小，因为列表大小一致

    xalex = range(1, datalen+1)
    if datalen <100:
        xalexstep = 10
    elif datalen>100 and datalen<1000:
        xalexstep = 100
    elif datalen>1000 and datalen<10000:
        xalexstep = 1000
    else:
        xalexstep = 1

    for mytitle in list(mydatadict.keys()):

        mindata = 10000000
        maxdata = 0
        fig1,ax = plt.subplots(1, 1, figsize=(12, 9))
        
        mykeylist = mydatadict[mytitle]

        for mykey in mykeylist:
            #print(mykey)
            if mykey in datakey:
                mydata = datadict[mykey]
                #print(mydata)
                mydata = list(map(float, mydata))
                #print(mydata)
                if max(mydata) > maxdata:
                    maxdata = max(mydata)

                if min(mydata) < mindata:
                    mindata = min(mydata)
                plt.plot(xalex,mydata,label=mykey)
         
        plt.ylim([mindata-5, maxdata+5])

        

        plt.xticks(xalex[::xalexstep])  # x坐标轴
        plt.xlabel("times")  # x轴
        plt.ylabel(myylabel)
        plt.title(mytitle)
        plt.legend(loc=0, numpoints=1)
        plt.legend(bbox_to_anchor=(1,-0.2), loc=0, borderaxespad=1,ncol=4) 
        #plt.legend(ncol=4)#图例分成两行
        plt.grid(alpha=0.1, linestyle="--")
        fig1.subplots_adjust(bottom=0.28)
                

        plt.savefig(mytitle+".png",dpi=160)  # 保存在当前目录中
        #plt.show()



if __name__=='__main__':
    import window_f
    import dataxlsread

    testinfo=window_f.test_info()

    filelisttemp = testinfo.select_file('select database','xls')
    datadict = dataxlsread.xlsread(filelisttemp,0,1,0)
    #print(datadict)

    filelisttemp = testinfo.select_file('select figue','xls')
    myfiguredict = dataxlsread.xlsread(filelisttemp,0,1,0)
    print(myfiguredict)

    #mydatadict={'温度':['中左吹面2','MAS8611_VEEE_CCM_Communication_Matrix_V5.0.1::BCM_410::NMBCM_SourceID','b']}
    genplot(datadict,myfiguredict,'temp')

    

    
