# -*- coding: utf-8 -*-

#dataxlswrite.py
#
#  ~~~~~~~~~~~~
#
#  Function write data into xls#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 20.05.2021
#  Last change: 24.05.2021 Li Yonghu 
#
#  Language: Python 3.7 
#  ------------------------------------------------------------------
#  GNU GPL
#  
 
#

# Module Imports

import os
import sys

import xlwt

import dataxlsread
import mapread
import datacsvread
import  traceback

def xlswrite(mapdict,datadict,flagrov,filepath):

    try:

        workbook = xlwt.Workbook(encoding = 'utf-8')
        worksheet = workbook.add_sheet('datasheet')
        
        loopnumcol = 0
        datalen = 10000000

        #listdatakey=list()

        #if flagrov:#romove more data
        for mykey in list(mapdict.keys()):
            loopnumrow = 0
            datakey = mapdict[mykey]

            if datakey in list(datadict.keys()):
                
                #listdatakey.append(datakey)
                mydata = datadict[datakey]
                datalentemp = len(mydata)
                if datalentemp < datalen:
                    datalen = datalentemp
##            else:
##                
##                listdatakey.append(mykey)
##                mydata = [0]*20000#temporary ,no work
                
                

        for mykey in list(mapdict.keys()):
            loopnumrow = 0
            #print(mykey)
            datakey = mapdict[mykey]

            if datakey in list(datadict.keys()):
                mydata = datadict[datakey]
                 
                worksheet.write(loopnumrow,loopnumcol,mykey)
                loopnumrow = loopnumrow+1
                

                if flagrov:

                    while loopnumrow<=datalen:
                        worksheet.write(loopnumrow,loopnumcol,mydata[loopnumrow-1])
                        loopnumrow = loopnumrow+1
                    loopnumcol =loopnumcol+1
                else:
                    for data in mydata:
                         worksheet.write(loopnumrow,loopnumcol,data)
                         loopnumrow = loopnumrow+1
                    loopnumcol =loopnumcol+1
            else:
                worksheet.write(loopnumrow,loopnumcol,mykey)
##                loopnumrow = loopnumrow+1
##
##                if flagrov:
##
##                    while loopnumrow<datalen:
##                        worksheet.write(loopnumrow,loopnumcol,0)
##                        loopnumrow = loopnumrow+1
                loopnumcol =loopnumcol+1  
                
                
        workbook.save(filepath+'\\Excel_DB.xls')
    except Exception as e:
        dblistmsgbox = traceback.print_exc()
        print(dblistmsgbox)
##
##    dbfile_display = 'save dbfile in: '+filepath+'\Excel_DB.xls'
##    print(dbfile_display)
##    return dbfile_display
    


if __name__=='__main__':
    import window_f
    import mapread
    from filter_file import filter_file

    oldpath=os.getcwd()

    testinfo=window_f.test_info()
    filepath_db=testinfo.select_dir('xls,xlsx or csv')
    os.chdir(filepath_db)
    filelist = os.listdir(os.getcwd())
    os.chdir(oldpath)

        

    filetype='.xls'
    flielist_xls = filter_file(filelist,filetype)
    #print(flielist_xls)

    filetype = '.csv'
    flielist_csv = filter_file(filelist,filetype)
    #print(flielist_csv)

    datadict = dict()

    for filelist in flielist_xls:
        filelisttemp = filepath_db+'\\'+ filelist
        datadicttemp = dataxlsread.xlsread(filelisttemp,0,1,1)
        datadict.update(datadicttemp)

    for filelist in flielist_csv:
        filelisttemp = filepath_db+'\\'+ filelist
        datadicttemp = datacsvread.csvread(filelisttemp)
        datadict.update(datadicttemp)

    #print(datadict)

    filepath = 'E:\\Project\\ProCCMTest\\DataManage'
    mapfile = testinfo.select_file('select map','xls')
    #print(mapfile)
    
    mapdict = mapread.mapread(mapfile)
    #print(mapdict)

    xlswrite(mapdict,datadict,True,filepath)
