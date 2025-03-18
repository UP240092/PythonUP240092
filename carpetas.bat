@echo off
for /l %%i in (3,1,20) do (
    setlocal enabledelayedexpansion
    set "num=0%%i"
    set "num=!num:~-2!"
    mkdir "!num!_Day"
    endlocal
)
echo Carpetas creadas exitosamente.
pause

