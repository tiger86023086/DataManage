@echo off
cd  %~dp0
cmd/k "pyinstaller -D -w -i "myico.ico" --distpath "../Released" -n "MainDataManage1.2" "MainDataManage1.2.py""