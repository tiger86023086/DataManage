# -*- coding: utf-8 -*-

import os
import mapread
from filter_file import filter_file
import datacsvread
import dataxlsread
import dataxlswrite

DataSFilePath = "E:/Project/ProCCMTest/DataManage/data"
MapFile = "E:/Project/ProCCMTest/DataManage/map/map.xls"
DBGenPath = "E:/Project/ProCCMTest/DataManage"

oldpath=os.getcwd()
filepath = str(DataSFilePath)
os.chdir(filepath)
filelist = os.listdir(os.getcwd())
os.chdir(oldpath)

filepath_db = DataSFilePath

filetype='.xls'
flielist_xls = filter_file(filelist,filetype)

filetype = '.csv'
flielist_csv = filter_file(filelist,filetype)

datadict = dict()

for filelist in flielist_xls:
    filelisttemp = filepath_db+'\\'+ filelist
    datadicttemp = dataxlsread.xlsread(filelisttemp,0,1,1)
    datadict.update(datadicttemp)

for filelist in flielist_csv:
    filelisttemp = filepath_db+'\\'+ filelist
    datadicttemp = datacsvread.csvread(filelisttemp)
    datadict.update(datadicttemp)


mapdict = mapread.mapread(MapFile)

dataxlswrite.xlswrite(mapdict,datadict,True,DBGenPath)

