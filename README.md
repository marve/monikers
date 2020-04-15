# Monikers

A team-based word guessing game for 4+ players. Intended for use over video conferencing.

## Requirements

* Python 3.6+
* Twilio Account (Free trial account is sufficient)

## Run the Code

These instructions will get you a copy of the project up and running on your local machine.

### Clone the repo

```bash
git clone https://github.com/marve/monikers.git
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Load virtual environment

```bash
source .venv/bin/activate
```

### Install Python dependencies

```bash
pip install -r requirements.txt
```

### Ensure tkinter is installed

```bash
sudo apt install python3-tk
```

### Set environment variables with Twilio credentials

```bash
export TWILIO_SID='abc123' # Use your Twilio SID.
export TWILIO_TOKEN='def456' # Use your Twilio auth token.
```

### Run the application

```bash
python src/main.py
```