# Monikers

A team-based word guessing game for 4+ players. Intended for use over video conferencing.

## Requirements

* Python 3.6+
* Twilio Account
  * Free trial account is sufficient, but you will have to pre-register every spymaster number.
* Ubuntu 18.04+ or Windows 10

## How does it work?

1. Follow steps in [Run the Code](README.md#run-the-code).
2. Gather phone numbers of players. _NOTE: This is optional but helps speed up game setup_.
3. Start/join a video conference with players. I recommend https://meet.jit.si/.
4. Share your screen.
5. Decide who will be the first spy master for each team and enter each spy master's phone number when prompted in the console. Each spy master will receive a SMS message with the grid key for the game.
6. Verify the spy masters received the messages. Use the in-game capability to resend if needed.
7. Once both spy masters have the grid key, the game board will draw on screen (this is why one person needs to share their screen).
8. Click on each word that is chosen. In a physical game, you might required the desired card to be touched. In a video conference you can ask the team to say "final answer" or something like that before you click the word.
9. The game runs in a loop so once the first game ends, pick new spy masters and play again.

## Run the Code

These instructions will get you a copy of the project up and running on your local machine.

### Clone the repo

```bash
git clone https://github.com/marve/monikers.git
```

### Linux

```bash
./start.sh
```

### Windows

_Must have installed python with tkinter included!_

```batch
start.cmd
```