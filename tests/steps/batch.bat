@ECHO OFF

SETLOCAL
SETLOCAL ENABLEDELAYEDEXPANSION

SET count=0
for %%o IN (D:\temp\*.*) DO (
      echo %%o
      SET /A count=count + 1
)

echo %count%

IF "%count%"=="100" ECHO NET STOP MyApp

ENDLOCAL ENABLEDELAYEDEXPANSION
ENDLOCAL