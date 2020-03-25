import csv
import random

words = []
with open('word-list/resources/wordlist.csv') as wordlist_csv:
  reader = csv.reader(wordlist_csv, delimiter=',', quotechar='"')
  for row in reader:
    words.append(row[0])

cards_per_game = 25
random.shuffle(words)
for idx in range(100):
  game_number = idx + 1
  input(f'Press <Enter> to generate a list of words for game {game_number}')
  start = idx * cards_per_game
  end = start + cards_per_game
  [print(w) for w in words[start:end]]