@echo off
if not exist "./binary\buffer" md "./binary\buffer"
for /f "delims=" %%i in ('dir /s /b "%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.htm"') do copy "%%i" "./binary\buffer"



