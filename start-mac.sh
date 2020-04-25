#!/bin/bash
VENV_DIR=".venv"
[ ! -d $VENV_DIR ] && python3 -m venv $VENV_DIR
source .venv/bin/activate
python -m pip install -r requirements.txt -q
read -p 'What is the Twilio SID? ' TWILIO_SID
read -sp 'What is the Twilio auth token? ' TWILIO_TOKEN
echo 
read -p 'What is the Twilio number? ' TWILIO_NUMBER
echo "Starting game. Press <Ctrl+C> followed by <Enter> to exit"
export TWILIO_SID
export TWILIO_TOKEN
export TWILIO_NUMBER
python src/main.py