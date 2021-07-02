@echo off
cd  %~dp0
cmd/k "pyinstaller -D -i "myico.ico" --distpath "../Released" -n "MainDataManage1.2_bt0" "MainDataManage1.2.py""