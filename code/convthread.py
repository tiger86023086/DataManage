# -*- coding: utf-8 -*-

#  convthread.py
#
#  ~~~~~~~~~~~~
#
#  Function convert mdf asc blf to csv Thread
#   Now asc blf converting do not work
# 
# 
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 01.07.2021
#  Last change: 01.07.2021 Li Yonghu 
#
#  Language: Python 3.7  PyQt5.15.2
#  ------------------------------------------------------------------
#  GNU GPL
#  
 
#

# Module Imports

from PyQt5.QtCore import (Qt,QThread,QMutex,QObject)
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import pyqtSlot as Slot
import time,os

from readmdf import readmdf
import pandas as pd
from filter_file import filter_file
import traceback

class CONVThread(QThread):
      finished2 = Signal(bool)
      stoped2 = Signal(bool)
      
      def __init__(self,parent=None):
            super(CONVThread,self).__init__(parent)           

            self.flgerror = False
            self.completed = False
            self.listmsgbox = ''
            self.stopped = False
            self.mymdf = readmdf()
      def init(self,
                incadatasrc,
                tgtdatapath,                                    
                 listmsgbox):
            self.incadatasrc = incadatasrc
            self.tgtdatapath = tgtdatapath
            
            self.listmsgbox = listmsgbox

      def stop(self):           
            self.stopped=True
            #self.wait()

      def isStopped(self):            
            return self.stopped
      def run(self):          
            sampletime = 5     
            reflag=self.DataConv(self.incadatasrc,
                                  self.tgtdatapath,
                                  sampletime,
                                  self.listmsgbox)
                  
            if reflag == True:
                  self.wait()
                  self.finished2.emit(self.completed)                  
            else:
                 self.wait()
            #self.result.emit(True)

      def DataConv(self,
                    incadatasrc,
                     tgtdatapath,
                     sampletime,                     
                     listmsgbox):

            try:
                if self.incadatasrc != '':
                    oldpath=os.getcwd()
                    filepath = str(incadatasrc)
                    os.chdir(filepath)
                    filelist = os.listdir(os.getcwd())
                    os.chdir(oldpath)                        
                        
                    filetype='.dat'
                    flielist_incadat = filter_file(filelist,filetype)
                    

                    filetype = '.mdf'
                    flielist_mdf = filter_file(filelist,filetype)
                if tgtdatapath != '':
                      for filelist in flielist_incadat:
                            filelistcsv = filelist.replace('.dat','.csv')
                            filelisttemp = filepath+'\\'+ filelist
                            filelisttemp1 = tgtdatapath+'\\'+filelistcsv
                            dblistmsgbox = 'Reading datasource '+filelisttemp
                            print(dblistmsgbox)
                            listmsgbox.append(dblistmsgbox)

                            res = self.mymdf.init(filelisttemp)
                            if res:
                                  res1 = self.mymdf.exportcsv(filelisttemp1,sampletime)
                                  if res1:
                                        mycsv = pd.read_csv(filelisttemp1)
                                        mycsv1 = mycsv.drop([0])
                                        mycsv1.to_csv(filelisttemp1,index=0)

                      for filelist in flielist_mdf:
                            filelistcsv = filelist.replace('.dat','.csv')
                            filelisttemp = filepath+'\\'+ filelist
                            filelisttemp1 = tgtdatapath+'\\'+filelistcsv
                            dblistmsgbox = 'Reading datasource '+filelisttemp
                            print(dblistmsgbox)
                            listmsgbox.append(dblistmsgbox)

                            res = self.mymdf.init(filelisttemp)
                            if res:
                                  res1 = self.mymdf.exportcsv(filelisttemp1,sampletime)
                                  if res1:
                                        mycsv = pd.read_csv(filelisttemp1)
                                        mycsv1 = mycsv.drop([0])
                                        mycsv1.to_csv(filelisttemp1,index=0)
                      return True
                    
            except Exception as e:
                  #self.flgerror = True
                  self.stoped.emit(True)
                  dblistmsgbox = traceback.print_exc()
                  print(dblistmsgbox)
                  self.listmsgbox.append(dblistmsgbox)
                  return False            