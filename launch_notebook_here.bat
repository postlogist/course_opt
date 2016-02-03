set WINP_ENV=c:\winpython32\scripts\env.bat

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
echo ERROR :  WINP_ENV must point to the 'env.bat' script file of winpython
echo .
echo syntax example : set WINP_ENV=C:\toto\WinPython-32bit-3.3.2.3\Scripts\env.bat 
echo .
echo please correct the first line of this script and try again
echo .
pause
exit

:no_Error_message
call "%winp_env%"
 
rem ** python2 or python3 case handling **
set                               variable_launch=ipython  notebook --pylab=inline
if "%WINPYVER%" GEQ "2.7.5.4" set variable_launch=ipython  notebook --matplotlib=inline
if "%WINPYVER%" GEQ "3.3.0.0" set variable_launch=ipython3 notebook --pylab=inline
if "%WINPYVER%" GEQ "3.3.2.2" set variable_launch=ipython3 notebook --matplotlib=inline


echo Winpython version is : %WINPYVER%
echo .
echo Notebook directory is :
echo     %~dp0
echo to check all is ok you can launch this in a notebook :
echo    print (get_ipython().profile_dir.location) "
echo .

@echo on
%WINPYDIR%\Scripts\%variable_launch%  --notebook-dir=%~dp0  


