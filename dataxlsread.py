# -*- coding: utf-8 -*-

#  dataxlsread.py
#
#  ~~~~~~~~~~~~
#
#  Function read data into dict
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
import traceback

def xlsread(filepath,tilerow,datarow,activecol,listmsgbox):
    
    
    wk = xlrd.open_workbook(filepath)
    sheet = wk.sheet_by_index(0)
    
    map_read_dict = xls_dict_create(sheet,tilerow,datarow,activecol,listmsgbox)
    
    return map_read_dict

def xls_dict_create(sheet,titlerow,datarow,activecol,listmsgbox):

    """
    titlerow: title row
    datarow: data row
    activecol:ture colme

    """
    colnum = sheet.ncols
    #print(colnum)
    rownum = sheet.nrows
    #print(rownum)
    map_read_dict={}
    loopnum=activecol
    

    try:

        while loopnum < colnum:
            colvalue = sheet.col_values(loopnum)
            #print(loopnum)
            if colvalue[titlerow] != '':
                loopnum1 = datarow
                listdata = list()

                while loopnum1 < rownum:
                    #print(colvalue[loopnum1])
                    #print(loopnum1)
                    listdata.append(colvalue[loopnum1])
                    loopnum1 = loopnum1+1
                #listdata.remove(listdata[0])
                map_read_dict[colvalue[titlerow]] = listdata
                
            else:
                pass
            loopnum = loopnum+1
    except Exception as e:
                  
              dblistmsgbox = traceback.print_exc()
              print(dblistmsgbox)
              listmsgbox.append(dblistmsgbox) 

    return map_read_dict

if __name__=='__main__':
    
     filepath = 'E:\\Project\\ProCCMTest\\DataManage\\Excel_test.xls'
     listmessagebox=''
     error=0
     mapdict = xlsread(filepath,0,1,0)
     print(mapdict)         
            
