@echo off
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

set "datestamp=%YYYY%%MM%%DD%"
set "timestamp=%HH%%Min%%Sec%"
set "filename=%datestamp%%timestamp%"

set "mainDirectory=C:\Users\msibtain.haider\Desktop\Python_Automation1\tests\allure-results"
for /f "skip=4 delims=" %%A in ('dir /b /ad /o-n "%mainDirectory%\*"')  do (
    rd /s /q "%mainDirectory%\%%~A"
)

cmd /k pytest --alluredir=C:\Users\msibtain.haider\Desktop\Python_Automation1\tests\allure-results\%filename%
