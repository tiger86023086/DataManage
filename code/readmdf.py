# -*- coding: utf-8 -*-

#  readmdf.py
#
#  ~~~~~~~~~~~~
#
#  Function read mdf(INCA/canape dat/mdf)
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 30.06.2021
#  Last change: 30.06.2021 Li Yonghu 
#
#  Language: Python 3.7 
#  ------------------------------------------------------------------
#  GNU GPL
#  
 
#

# Module Imports

import mdfreader
import sys
import traceback

class readmdf:    
    def init(self,srcfullname):
        try:
            self.yop=mdfreader.Mdf(srcfullname)
            return True
        except Exception as e:
            mylistmsgbox = traceback.print_exc()
            print(mylistmsgbox)
            return False 
    def exportcsv(self,tgtpath,sampletime):
        try:
            self.yop.export_to_csv(file_name=tgtpath,sampling=sampletime)
            return True
        except Exception as e:
            mylistmsgbox = traceback.print_exc()
            print(mylistmsgbox)
            return False

if __name__=='__main__':
    import os
    #oldpath=os.getcwd()
    srcfullname = 'E:\\Project\\ProCCMTest\\DataManage\\code\\data\\incadata\\demo.dat'
    datanametemp = srcfullname.split('\\')[-1]
    dataname = datanametemp.replace('.dat','')
    tgtpath = 'E:\\Project\\ProCCMTest\\DataManage\\code\\data\\incadata\\'+dataname+'.csv'
    sampletime = 5
    mymdf = readmdf()
    res = mymdf.init(srcfullname)
    if res:
        #os.chdir(tgtpath)
        res1 = mymdf.exportcsv(tgtpath,sampletime)
        #os.chdir(oldpath)
    