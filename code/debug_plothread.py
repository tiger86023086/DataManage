# -*- coding: utf-8 -*-

from filter_file import filter_file
import genplot
import dataxlsread

DataSFilePath = "E:/Project/ProCCMTest/DataManage/data"
MapFile = "E:/Project/ProCCMTest/DataManage/map/map.xls"
DBGenPath = "E:/Project/ProCCMTest/DataManage"

datadict = dataxlsread.xlsread(DBFile,0,1,0)

myfiguredict = dataxlsread.xlsread(TitleFile,0,1,0)

genplot.genplot(datadict,myfiguredict,'temp')

