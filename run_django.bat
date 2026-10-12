@echo off
echo ==========================================
echo  Spustanie Django aplikacie (automaticky)
echo ==========================================
echo.

:: Presun do priecinka, kde sa nachadza tento subor
cd /d "%~dp0"

:: Skontroluj, ci existuje venv, ak nie, vytvor ho
if not exist ".venv" (
    echo Vytvaram virtualne prostredie...
    py -3 -m venv .venv
)

:: Aktivuj venv
echo Aktivujem virtualne prostredie...
call ".venv\Scripts\activate.bat"

:: Aktualizuj pip
echo Aktualizujem pip...
python -m pip install --upgrade pip >nul

:: Instaluj Django, len ak chyba
echo Kontrolujem potrebne balicky...
python -m pip show django >nul 2>&1 || python -m pip install django

:: Spusti aplikaciu
echo.
echo ==========================================
echo Spustam Django aplikaciu...
echo ==========================================
echo.

python manage.py runserver

:: Po vypnuti servera deaktivuj venv
deactivate

echo.
echo ==========================================
echo Django server bol ukonceny.
echo Stlac lubovolnu klavesu pre zatvorenie okna.
echo ==========================================
pause