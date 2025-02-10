@echo off
title 井字棋卸载向导
echo 即将为你卸载井字棋
pause
del "%USERPROFILE%\Desktop\井字棋.lnk"
rd /s /q %cd%
echo 卸载完毕！
pause