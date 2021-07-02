# -*- coding: utf-8 -*-

#filter_file.py
#
#  ~~~~~~~~~~~~
#
#  Function filter the file type one file
#
#  ~~~~~~~~~~~~
#
#  ------------------------------------------------------------------
#  Author : Li Yonghu
#  Build: 24.05.2021
#  Last change: 24.05.2021 Li Yonghu 
#
#  Language: Python 3.7 
#  ------------------------------------------------------------------
#  GNU GPL
#  
 
#

# Module Imports

def filter_file(filelist,filetype):
    filelist_name=[]
    for file_name in filelist:
        if file_name.find(filetype)>0 and file_name.find('$')<0:
            filelist_name.append(file_name)
##                self.fileinfo.xlsname.append(file_name)  #append xlsname
        else:
            pass
    return filelist_name
