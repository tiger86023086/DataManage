# -*- coding: utf-8 -*-

##import csv
##
##def hebing(dic1,dic3):
##    for key in dic1:
##        if dic3.get(key):
##            dic3[key].append(dic1[key])
##        else:
##            dic3[key]=[dic1[key]]
##    return dic3
##
##def Merge(dict1,dict2):
##    dict1.update(dict2)
##    return(dict1)
##
##if __name__=='__main__':
##    mapdict=dict()
##
##    with open('E:\\Project\\ProCCMTest\\DataManage\\------ 无阳光 AUTO22 PTCAN.csv','r') as csvfile:
##    ##    csvreader = csv.reader(csvfile)
##    ##    
##    ##    aa=list(csvreader)
##    ##    aa[0].remove(aa[0][0])
##    ##    print(aa[0])
##    ##    for dictkey in 
##    ##    
##    ####    for num in range(len(csvreader)):
##    ####        print()
##        fcsv = csv.DictReader(csvfile)
##        for row in fcsv:
##            mapdict = hebing(row,mapdict)
##            #mapdict.update(row)
##            #print(row)
##    print(mapdict)
        


from matplotlib import pyplot as plt
#from matplotlib import font_manager


# 设置图片大小和分辨率
fig=plt.figure(figsize=(8, 6), dpi=160)

#ResNet18不冻结数据
a1=[0.94,0.93,0.91,0.94,0.92,0.94,0.93,0.91,0.91,0.94]
b1=[0.6,0.93,0.91,0.7,0.92,0.94,0.9,0.91,0.91,0.8]


x = range(1, 11)#设置横坐标范围，这里要与上面a1中的数据个数相对应
plt.plot(x, a1,label='a1')
plt.plot(x, b1,label='b1')
plt.ylim([0.6, 1])#设置y轴显示范围从0.8到1
# 绘制折线图


plt.xticks(x[::1])  # x坐标轴
# 描述内容信息
plt.xlabel("times")  # x轴
plt.ylabel("Testing Accuracy")  # y轴
plt.title("CNN")
plt.text(3, 0.85, "average value:92.7%", size = 15, alpha = 0.2)


# 绘制网格
plt.grid(alpha=0.1, linestyle="--")

plt.savefig("1.png")  # 保存在当前目录中
plt.show()

