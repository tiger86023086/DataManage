# -*- coding: utf-8 -*-

#  plothread.py
#
#  ~~~~~~~~~~~~
#
#  Function GUI Generate Plot Thread
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

from filter_file import filter_file
import genplot
import dataxlsread


class PlotThread(QThread):
      finished1 = Signal(bool)
      stoped1 = Signal(bool)
      
      def __init__(self,parent=None):
            super(PlotThread,self).__init__(parent)           

            self.error = False
            self.completed = False
            self.listmsgbox = ''
            self.stopped1 = False
            
            #self.a2lpath=None      
            
      def initialize(self,
                     DBFile,
                     TitleFile,
                     listmsgbox):

            self.DBFile = DBFile
            self.TitleFile = TitleFile
            self.listmsgbox = listmsgbox
                  

      def stop(self):
           
            self.stopped1=True
            #self.wait()

      def isStopped(self):
            
            return self.stopped1
            

      def run(self):          
                  
            reflag=self.PlotCreate(self.DBFile,
                                 self.TitleFile)
                  
            if reflag == True:
                  self.wait()
                  self.finished1.emit(self.completed)
                  
            else:
                 self.wait()

            #self.result.emit(True)

      def PlotCreate(self,
                   DBFile,
                   TitleFile):

            try:
                  if DBFile != '' and TitleFile != '':

                        if self.isStopped():
                              return False
                        
                        datadict = dataxlsread.xlsread(DBFile,0,1,0)
                        myfiguredict = dataxlsread.xlsread(TitleFile,0,1,0)
                        genplot.genplot(datadict,myfiguredict,'temp')                  

                        self.completed = True
                        dblistmsgbox = 'Plot File is be created '
                        print(dblistmsgbox)
                        self.listmsgbox.append(dblistmsgbox)
                        return True
                  else:
                        #self.error = True
                        self.stoped1.emit(True)
                        dblistmsgbox = 'DB file path or Figure file is None'
                        print(dblistmsgbox)
                        self.listmsgbox.append(dblistmsgbox)
                        
            
            except Exception as e:
                  self.stoped1.emit(True)
                  dblistmsgbox = traceback.print_exc()
                  print(dblistmsgbox)
                  self.listmsgbox.append(dblistmsgbox)
                  return False
