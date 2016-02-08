set WINPYTHON=c:\winpython32
set WINP_ENV=%WINPYTHON%\scripts\env.bat
set winp_env

chcp 1251

@echo off
rem ************************************
rem usage : 
rem    * 'set WINP_ENV=' must point to "a" winpython env.bat script
rem           (in "your WinPython base directory"\Scripts\env.bat )
rem    * place it in any directory with .ipynb  
rem    * double-click on it to launch the ipython notebook 
rem ************************************

rem ** check error (or not  parametrized yet)
set error_info="%WINP_ENV%" not ok
if exist "%WINP_ENV%"  goto no_Error_message

:Error_message
echo .
echo Ошибка :  Укажите правильный путь к папке с WinPython в первой строке этого файла!
echo .
echo например : set WINPYTHON=C:\WinPython32 
echo .
pause
exit

:no_Error_message
call "%winp_env%"
 
echo Версия WinPython: %WINPYVER%
echo .
echo Папка с блокнотами:
echo     %~dp0
echo для проверки можно выполнить в блокноте команду:
echo    print (get_ipython().profile_dir.location) "
echo .

@echo on
%WINPYTHON%\scripts\ipython_notebook --notebook-dir=%~dp0
