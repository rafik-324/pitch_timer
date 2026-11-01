@echo off
rem Startet den Pitch Timer auf 127.0.0.1 und oeffnet den Browser.
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 serve.py %*
  goto :end
)

python --version >nul 2>nul
if %errorlevel%==0 (
  python serve.py %*
  goto :end
)

echo Python wurde nicht gefunden. Bitte Python 3 von python.org installieren.
pause

:end
