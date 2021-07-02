# -*- coding: utf-8 -*-

#  datacsvread.py
#
#  ~~~~~~~~~~~~
#
#  Function csv read ,output dict
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 20.05.2021
#  Last change: 20.05.2021 Li Yonghu 
#
#  Language: Python 3.7 
#  ------------------------------------------------------------------
#  GNU GPL
#  
 
#

# Module Imports

import csv
import sys
import traceback


def hebing(dic1,dic3):
    for key in dic1:
        if dic3.get(key):
            dic3[key].append(dic1[key])
        else:
            dic3[key]=[dic1[key]]
    return dic3

def csvread(filecsvpath,listmsgbox):
     mapdict = dict()
     
     try:
         with open(filecsvpath,'r',encoding='gbk') as csvfile:
            
        
            #fcsv = csv.DictReader(csvfile,encoding="ISO-8859-1")
            fcsv = csv.DictReader(csvfile)
            #fcsv = fcsv.encoding('gbk')
            
            for row in fcsv:
                mapdict = hebing(row,mapdict)
                #mapdict.update(row)
                #print(row)

     except Exception as e:
                  
            dblistmsgbox = traceback.print_exc()
            print(dblistmsgbox)
            listmsgbox.append(dblistmsgbox)
     return mapdict

if __name__=='__main__':
    listmsgbox = []
    mapdict=csvread('E:\\Project\\ProCCMTest\\DataManage\\map\\210425 10-20°C 无阳光 AUTO 双区 带吹面吹脚  BDCAN.csv',listmsgbox)
    print(mapdict)
