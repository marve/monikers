import csv
import random

words = []
with open('game-board/resources/wordlist.csv') as wordlist_csv:
  reader = csv.reader(wordlist_csv, delimiter=',', quotechar='"')
  for row in reader:
    words.append(row[0])

cards_per_game = 25
random.shuffle(words)

### Assume game_number starts at 0
def get_word_set(game_number):
  start = game_number * cards_per_game
  end = start + cards_per_game
  return words[start:end]