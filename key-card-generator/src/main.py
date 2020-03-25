from PIL import Image
from typing import List
import random

red_border_path = 'key-card-generator/resources/red-border.png'
blue_border_path = 'key-card-generator/resources/blue-border.png'
blue = Image.open('key-card-generator/resources/blue.png', 'r')
red = Image.open('key-card-generator/resources/red.png', 'r')
neutral = Image.open('key-card-generator/resources/neutral.png', 'r')
assassin = Image.open('key-card-generator/resources/assassin.png', 'r')

tile_padding = 2
border_margin = 37
tile_size = 26
base_tiles = [assassin] + [neutral for _ in range(7)]
random.seed(0)

class KeyGrid:
  border: Image = None
  tiles: List = []

  def __init__(self, border: Image, tiles: List):
    self.border = border
    self.tiles = tiles

  def draw(self, out_path: str):
    grid = Image.new('RGBA', (216, 216), color = 'black')
    grid.paste(self.border)
    for row in range(5):
      start = row * 5
      end = start + 5
      y = border_margin + ((row + 1) * tile_padding) + (row * tile_size)
      for idx, tile in enumerate(self.tiles[start:end]):
        x = border_margin + ((idx + 1) * tile_padding) + (idx * tile_size)
        grid.paste(tile, (x, y))
    grid.save(out_path)

def make_red_grid() -> KeyGrid:
  tiles = base_tiles + [red for _ in range(9)] + [blue for _ in range(8)]
  border_image = Image.open(red_border_path, 'r')
  random.shuffle(tiles)
  return KeyGrid(border_image, tiles)

def make_blue_grid() -> KeyGrid:
  tiles = base_tiles + [red for _ in range(8)] + [blue for _ in range(9)]
  border_image = Image.open(blue_border_path, 'r')
  random.shuffle(tiles)
  return KeyGrid(border_image, tiles)

for idx in range(40):
  if random.randint(0, 1):
    grid = make_blue_grid()
  else:
    grid = make_red_grid()
  grid.draw(f'grid-{idx}.png')