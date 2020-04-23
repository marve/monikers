#!/bin/bash
VENV_DIR=".venv"
[ ! -d $VENV_DIR ] && python3 -m venv $VENV_DIR
source .venv/bin/activate
python -m pip install -r requirements.txt -q
sudo apt install python3-tk -y
echo "Starting game. Press Ctrl+C followed by Y and then Enter to exit"
read -p 'Username: ' uservar
read -sp 'Password: ' passvar