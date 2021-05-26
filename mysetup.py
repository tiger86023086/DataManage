# -*- coding: utf-8 -*-
#my setup.py

from distutils.core import setup
import py2exe
import sys
#from PyQt5 import sip

sys.argv.append('py2exe')

py2exe_options={
    "includes":["PyQt5.sip"],
    "dll_excludes":["MSVCP90.dll",
                    "QT5CORE.DLL",
                    "PYTHON3.DLL",
                    "KERNEL32.DLL",
                    "VCRUNTIME140.DLL",                    
                    "API-MS-WIN-CRT-RUNTIME-L1-1-0.DLL",
                    "API-MS-WIN-CRT-HEAP-L1-1-0.DLL",
                    "API-MS-WIN-CRT-ENVIRONMENT-L1-1-0.DLL",
                    "API-MS-WIN-CRT-STDIO-L1-1-0.DLL",
                    "API-MS-WIN-CRT-TIME-L1-1-0.DLL",
                    "API-MS-WIN-CRT-MATH-L1-1-0.DLL",
                    "API-MS-WIN-CRT-STRING-L1-1-0.DLL",
                    "API-MS-WIN-CRT-UTILITY-L1-1-0.DLL",
                    "API-MS-WIN-CRT-CONVERT-L1-1-0.DLL",
                    "API-MS-WIN-CRT-FILESYSTEM-L1-1-0.DLL",
                    "api-ms-win-core-registry-l1-1-0.dll",
                    "api-ms-win-core-string-obsolete-l1-1-0.dll",
                    "api-ms-win-core-string-l2-1-0.dll",
                    "api-ms-win-security-base-l1-1-0.dll",
                    "api-ms-win-core-psapi-l1-1-0.dll",
                    "api-ms-win-core-delayload-l1-1-0.dll",
                    "api-ms-win-core-libraryloader-l1-2-1.dll",
                    "api-ms-win-core-heap-obsolete-l1-1-0.dll",
                    "api-ms-win-core-atoms-l1-1-0.dll",
                    "api-ms-win-core-heap-l2-1-0.dll",
                    "api-ms-win-core-delayload-l1-1-1.dll",
                    "api-ms-win-core-com-midlproxystub-l1-1-0.dll",
                    "api-ms-win-core-libraryloader-l1-2-0.dll",
                    "api-ms-win-core-threadpool-legacy-l1-1-0.dll"],
      "compressed":1,
      "optimize":2,
      "ascii":0,
      "bundle_files":3,
      }
setup(
      name = 'Data Manage',
      version = '1.1',
      windows = [{'script':'MainDataManage1.1.py','icon_resources':[(1,'myico.ico')]}],
      #zipfile = None,
      #options = {'py2exe':{"includes":["sip"]}}
      options = {'py2exe':py2exe_options}
      
      )
#distutils.core.setup(windows=[{'script':'MainCreate.py','icon_resources':[(1,'timgCADXKVUY.ico')]}])

