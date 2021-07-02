# -*- coding: utf-8 -*-

#  dbthread.py
#
#  ~~~~~~~~~~~~
#
#  Function GUI DB Thread
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 24.05.2021
#  Last change: 24.05.2021 Li Yonghu 
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

import mapread
from filter_file import filter_file
import datacsvread
import dataxlsread
import dataxlswrite
import traceback


class DBThread(QThread):
      finished = Signal(bool)
      stoped = Signal(bool)
      
      def __init__(self,parent=None):
            super(DBThread,self).__init__(parent)           

            self.flgerror = False
            self.completed = False
            self.listmsgbox = ''
            self.stopped = False
            
            #self.a2lpath=None      
            
      def initialize(self,
                     DataSFilePath,
                     MapFile,
                     DBGenPath,
                     listmsgbox):

            self.DataSFilePath = DataSFilePath
            self.MapFile = MapFile
            self.DBGenPath = DBGenPath
            self.listmsgbox = listmsgbox
            #self.flgerror = flgerror

      def stop(self):           
            self.stopped=True
            #self.wait()

      def isStopped(self):
            
            return self.stopped
            

      def run(self):          
                  
            reflag=self.DBCreate(self.DataSFilePath,
                                 self.MapFile,
                                 self.DBGenPath)
                  
            if reflag == True:
                  self.wait()
                  self.finished.emit(self.completed)                  
            else:
                 self.wait()
            #self.result.emit(True)

      def DBCreate(self,
                   DataSFilePath,
                   MapFile,
                   DBGenPath):
            #print(DataSFilePath)

            #self.listmsgbox.append('aaaaaaaaaa')

            try:
                  if DataSFilePath != '' and MapFile != '' and DBGenPath != '':                        

                        oldpath=os.getcwd()
                        filepath = str(DataSFilePath)
                        os.chdir(filepath)
                        filelist = os.listdir(os.getcwd())
                        os.chdir(oldpath)                        

                        #filepath_db = DataSFilePath
                        
                        filetype='.xls'
                        flielist_xls = filter_file(filelist,filetype)

                        filetype = '.csv'
                        flielist_csv = filter_file(filelist,filetype)                        

                        datadict = dict()

                        if self.isStopped():
                              return False

                        

                        for filelist in flielist_xls:
                              filelisttemp = filepath+'\\'+ filelist
                              
                              dblistmsgbox = 'Reading datasource '+filelisttemp
                              print(dblistmsgbox)
                              self.listmsgbox.append(dblistmsgbox)
                              
                              datadicttemp = dataxlsread.xlsread(filelisttemp,0,1,1,self.listmsgbox)
                              
                              datadict.update(datadicttemp)                              

                        for filelist in flielist_csv:
                              filelisttemp = filepath+'\\'+ filelist

                              dblistmsgbox = 'Reading datasource '+filelisttemp
                              print(dblistmsgbox)
                              self.listmsgbox.append(dblistmsgbox)
                              
                              #self.listmsgbox.append('aaaaaaaaaa')
                              datadicttemp = datacsvread.csvread(filelisttemp,self.listmsgbox)
                              datadict.update(datadicttemp)
                              #self.listmsgbox.append('bbbbbbbbbb')

                        mapdict = mapread.mapread(MapFile)

                        dataxlswrite.xlswrite(mapdict,datadict,True,DBGenPath)

                        self.completed = True
                        dblistmsgbox = 'DB File is be created at '+DBGenPath
                        print(dblistmsgbox)
                        self.listmsgbox.append(dblistmsgbox)
                        return True
                  else:
                      #self.flgerror = True
                      self.stoped.emit(True)
                      dblistmsgbox = 'DB Soure path or map file path or DB Generate path is None'
                      print(dblistmsgbox)
                      self.listmsgbox.append(dblistmsgbox)                     
                      
            
            except Exception as e:
                  #self.flgerror = True
                  self.stoped.emit(True)
                  dblistmsgbox = traceback.print_exc()
                  print(dblistmsgbox)
                  self.listmsgbox.append(dblistmsgbox)
                  return False
