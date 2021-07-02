# -*- coding: utf-8 -*-

#  MainDataManage.py
#
#  ~~~~~~~~~~~~
#
#  Function GUI MainWindow Thread
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 24.05.2021
#  Last change: 30.06.2021 Li Yonghu 
#
#  Language: Python 3.7  PyQt5.15.2
#  ------------------------------------------------------------------
#  GNU GPL
#  
 
#

# Module Imports

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
#from future_builtins import *


from PyQt5.QtCore import (Qt,QTimer,QReadWriteLock,QDir)
from PyQt5.QtCore import pyqtSignal as Signal
from PyQt5.QtCore import pyqtSlot as Slot
from PyQt5.QtWidgets import (QApplication, QMainWindow,QDialog,QFileDialog,QWidget,QAction,QMessageBox)
import ui_MainWindow

import qdarkstyle  # noqa: E402
from qdarkstyle.dark.palette import DarkPalette  # noqa: E402
from qdarkstyle.light.palette import LightPalette  # noqa: E402

import os,sys

import plothread
import dbthread
import convthread


class MainWin(QMainWindow,
           ui_MainWindow.Ui_DataAnalysis):      

      def __init__(self,parent=None):
            super(MainWin,self).__init__(parent)
            self.listmsgbox=list()
            self.flgerror=False

            self.incadatasrc = ''
            self.tgtdatapath = ''

            self.DataSource = ''
            self.Mapdirfile = ''
            self.DBPath = ''

            self.DBdirfile = ''
            self.TLdirfile = ''

            self.thread=dbthread.DBThread()
            self.thread1=plothread.PlotThread()
            self.thread2=convthread.CONVThread()            

            self.timer=QTimer(self)
            self.timer.timeout.connect(self.showtime)

            self.timer1=QTimer(self)
            self.timer1.timeout.connect(self.showtime1)

            self.thread.finished.connect(self.finished)
            #self.thread1.result.connect(self.hsresult)
            self.thread.stoped.connect(self.stoped)

            self.thread1.finished1.connect(self.finished1)
            #self.thread1.result.connect(self.hsresult)
            self.thread1.stoped1.connect(self.stoped1)

            self.thread2.finished2.connect(self.finished2)           
            
            self.setupUi(self)

      @Slot()
      def on_actionDarkStyle_triggered(self):
            #print('aa')
            style = qdarkstyle.load_stylesheet(palette=DarkPalette)
            self.setStyleSheet(style)                       

      @Slot()            
      def on_actionLightStyle_triggered(self):
            #print('bb')
            style = qdarkstyle.load_stylesheet(palette=LightPalette)
            self.setStyleSheet(style)            
      	    
      @Slot()
      def on_pushButtonDataSo_clicked(self):

            self.DataSource=QFileDialog.getExistingDirectory(self,"Select Data Source",os.getcwd(),QFileDialog.DontResolveSymlinks)
            self.lineEditDataSource.setText(self.DataSource)       

      @Slot()
      def on_pushButtonMapFile_clicked(self):
            
            self.Mapdirfile,filetype=QFileDialog.getOpenFileName(self,
                                                    "Select Map File",
                                                    os.getcwd(),
                                                    "Map Files (*.xls);;Map Files (*.xlsx)")
            
            self.lineEditMapFile.setText(self.Mapdirfile)
            
      @Slot()
      def on_pushButtonDBPath_clicked(self):            

            self.DBPath=QFileDialog.getExistingDirectory(self,"Select DB Genreate Path",os.getcwd(),QFileDialog.DontResolveSymlinks)
            self.lineEditDBPath.setText(self.DBPath)

      @Slot()
      def on_pushButtonStartD_clicked(self):            
            self.thread.initialize(self.DataSource,
                                   self.Mapdirfile,
                                   self.DBPath,
                                   self.listmsgbox)

            self.thread.start()
            self.timer.start(1)

            self.pushButtonStartD.setEnabled(False)
            
      @Slot()
      def on_pushButtonStopD_clicked(self):
            self.thread.wait()
            self.timer.stop()

      @Slot()
      def on_pushButtonClearD_clicked(self):

            self.thread.wait()
            self.timer.stop()

            self.textBrowserD.clear()

            self.DataSource = ''
            self.lineEditDataSource.setText("")

            self.Mapdirfile = ''
            self.lineEditMapFile.setText("")            

            self.DBPath = ''
            self.lineEditDBPath.setText("")

            self.pushButtonStartD.setEnabled(True)

      @Slot()
      def on_pushButtonDBFile_clicked(self):
            
            self.DBdirfile,filetype=QFileDialog.getOpenFileName(self,
                                                    "Select DB File",
                                                    os.getcwd(),
                                                    "DB Files (*.xls);;DB Files (*.xlsx)")
            
            self.lineEditDBFile.setText(self.DBdirfile)

      @Slot()
      def on_pushButtonTitleFile_clicked(self):
            
            self.TLdirfile,filetype=QFileDialog.getOpenFileName(self,
                                                    "Select Title File",
                                                    os.getcwd(),
                                                    "Title Files (*.xls);;Title Files (*.xlsx)")
            
            self.lineEditTitleFile.setText(self.TLdirfile)


      @Slot()
      def on_pushButtonStartP_clicked(self):
            print(self.DBdirfile)
            print(self.TLdirfile)

            self.thread1.initialize(self.DBdirfile,
                                   self.TLdirfile,
                                    self.listmsgbox)
            self.thread1.start()
            self.timer1.start(1)
            
      @Slot()
      def on_pushButtonStopP_clicked(self):
            self.thread1.wait()
            self.timer1.stop()

      @Slot()
      def on_pushButtonClearP_clicked(self):

            self.thread1.wait()
            self.timer1.stop()

            self.textBrowserP.clear()
            
            self.DBdirfile = ''
            self.lineEditDBFile.setText("")

            self.TLdirfile = ''
            self.lineEditTitleFile.setText("")            

      def showtime(self):

            self.textBrowserD.clear()

            for prt in self.listmsgbox:
                  self.textBrowserD.append(prt)

      def finished(self, completed):

            self.timer.stop()
            self.textBrowserD.append("All  are complete !!!")
            self.listmsgbox=list()
            self.pushButtonStartD.setEnabled(True)

            QMessageBox.information(self, "完成", "处理成功",
                                    QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )

      def stoped(self):

            self.listmsgbox=list()
            self.timer.stop()
            self.textBrowserD.append("There is some error!")            
            self.thread.wait()
            QMessageBox.critical(self,"错误","严重错误",
                                 QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes)

      def showtime1(self):

            self.textBrowserP.clear()

            for prt in self.listmsgbox:
                  self.textBrowserP.append(prt)

      def finished1(self, completed):

            self.timer1.stop()
            self.textBrowserP.append("All  are complete !!!")
            self.listmsgbox=list()
            self.pushButtonStartP.setEnabled(True)

            QMessageBox.information(self, "完成", "处理成功",
                                    QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )

      def stoped1(self):

            self.listmsgbox=list()
            self.timer1.stop()
            self.textBrowserP.append("There is some error!")            
            self.thread1.wait()
            QMessageBox.critical(self,"错误","严重错误",
                                 QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes)
      @Slot()
      def on_pushButtonDateFile_clicked(self):
            self.incadatasrc=QFileDialog.getExistingDirectory(self,"Select INCA/CANape logData Source",os.getcwd(),QFileDialog.DontResolveSymlinks)
            self.lineEditDateFile.setText(self.incadatasrc)
      @Slot()
      def on_pushButtonTgtFile_clicked(self):
            self.tgtdatapath=QFileDialog.getExistingDirectory(self,"Select  generate csv path",os.getcwd(),QFileDialog.DontResolveSymlinks)
            self.lineEditTgtFile.setText(self.tgtdatapath)
      @Slot()
      def on_pushButtonDataCon_clicked(self):
            self.thread2.init(self.incadatasrc,
                                   self.tgtdatapath,
                                    self.listmsgbox)
            self.thread2.start()
      def finished2(self):
             QMessageBox.information(self, "完成", "处理成功",
                                    QMessageBox.Yes | QMessageBox.No ,  QMessageBox.Yes )
            

if __name__ == "__main__":
    import sys

    QApplication.addLibraryPath("./plugins")

    app = QApplication(sys.argv)
    form=MainWin()
    form.show()
    sys.exit(app.exec_())
