if [%1]==[] goto usage
if [%2]==[] goto usage
echo registration_url=%~1 > configuration.properties
echo sumo_logic_url=%~2 >> configuration.properties
pyinstaller --onefile --icon "mdm_icon.ico" --add-data "configuration.properties;." src\winzog.py
goto :eof

:usage
@echo Usage: %0 ^<Registration App URL^> ^<Sumo Logic Url^>
exit /B 1