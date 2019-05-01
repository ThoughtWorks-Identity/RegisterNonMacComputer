if [%1]==[] goto usage
echo %1 > registrationWebAppUrl.txt
pyinstaller --onefile --noconsole --icon "mdm_icon.ico" --add-data "registrationWebAppUrl.txt;." src\winzog.py
goto :eof

:usage
@echo Usage: %0 ^<Registration App URL^>
exit /B 1