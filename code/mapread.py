# -*- coding: utf-8 -*-

#  mapread.py
#
#  ~~~~~~~~~~~~
#
#  Function read map into dict
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

import xlrd
import sys

def mapread(filepath):
    
    wk = xlrd.open_workbook(filepath)
    sheet = wk.sheet_by_index(0)
    map_read_dict = map_dict_create(sheet)
    
    return map_read_dict

def map_dict_create(sheet):

    row_num=sheet.nrows
    map_read_dict={}
    loopnum=1

    while loopnum < row_num:

        rowvalue=sheet.row_values(loopnum)
        if rowvalue[1] != '':
            map_read_dict[rowvalue[1]] = rowvalue[2]
        else:
            pass
        loopnum = loopnum+1
    return map_read_dict

if __name__=='__main__':
    
     filepath = 'E:\\Project\\ProCCMTest\\DataManage\\map\\MAP.xlsx'
     listmessagebox=''
     error=0
     mapdict = mapread(filepath)
     print(mapdict)            
        
    
