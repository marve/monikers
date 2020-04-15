import csv
import random
from autocorrect import Speller

words = []
with open('resources/wordlist.csv') as wordlist_csv:
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

if __name__== "__main__":
  spell = Speller(lang='en')
  for idx, word in enumerate(words):
    if word != spell(word):
      input(f'[{idx} of {len(words)}] Perhaps {word} should actually be {spell(word)}?')