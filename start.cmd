@echo on
set VENV_DIR=.venv
if exist %VENV_DIR% (
  echo "Re-using existing venv"
) else (
  python -m venv %VENV_DIR%
)
call %VENV_DIR%\scripts\activate.bat
python -m pip install -r requirements.txt -qq
set /p TWILIO_SID="What is the Twilio SID? "
Call:InputPassword "What is the Twilio auth token? " TWILIO_TOKEN
set /p TWILIO_NUMBER="What is the Twilio number? "
echo Starting game. Press <Ctrl+C> followed by <Y> and then <Enter> to exit
python src/main.py
pause
::***********************************
:InputPassword
set "psCommand=powershell -Command "$pword = read-host '%1' -AsSecureString ; ^
    $BSTR=[System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($pword); ^
      [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)""
        for /f "usebackq delims=" %%p in (`%psCommand%`) do set %2=%%p
)
goto :eof
::***********************************