@echo off

for /f %%I in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd_HH-mm-ss"') do set timestamp=%%I

robot --outputdir "C:\Users\USER\saucedemo_ui_automation\Reports\%timestamp%" C:\Users\USER\saucedemo_ui_automation\Usecases\execution_file.robot
