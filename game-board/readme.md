# game-board
Build a game board
word_list.py: CLI tool to generate words for game play.
keycard_generator: CLI tool to generate grid keys for game play.


## Setup development environment
__Requires Python 3.6+__
__Requires Twilio Account__

1. Create a virtual environment. 
```
python3 -m venv .venv
```
2. Load virtual environment.
```
source .venv/bin/activate
```
3. Install dependencies.
```
pip install -r game-board/requirements.txt
```
4. Ensure tkinter is installed.
```
sudo apt install python3-tk
```
5. Set environment variables with Twilio credentials.
```
export TWILIO_SID='abc123' # Use your Twilio SID.
export TWILIO_TOKEN='def456' # Use your Twilio auth token.
```