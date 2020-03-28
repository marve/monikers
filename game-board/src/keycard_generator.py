from PIL import Image, ImageDraw
from typing import List
import random
import pickle
from enum import Enum

resource_path = 'game-board/resources'
generated_path = f'{resource_path}/generated/grid-'
red_border_path = f'{resource_path}/red-border.png'
blue_border_path = f'{resource_path}/blue-border.png'
blue = Image.open(f'{resource_path}/blue.png', 'r')
red = Image.open(f'{resource_path}/red.png', 'r')
neutral = Image.open(f'{resource_path}/neutral.png', 'r')
assassin = Image.open(f'{resource_path}/assassin.png', 'r')

tile_padding = 2
border_margin = 37
tile_size = 26
random.seed()

class TileType(Enum):
  NEUTRAL = 1,
  ASSASSIN = 2,
  RED = 3,
  BLUE = 4

class Tile:
  tile_type: TileType
  image: Image

  def __init__(self, tile_type, image):
    self.tile_type = tile_type
    self.image = image

base_tiles = [Tile(TileType.ASSASSIN, assassin)] + [Tile(TileType.NEUTRAL, neutral) for _ in range(7)]

class KeyGrid:
  border: Image = None
  tiles: List = []

  def __init__(self, border: Image, tiles: List):
    self.border = border
    self.tiles = tiles

  def draw(self, out_path: str):
    grid = Image.new('RGBA', (216, 216), color = 'black')
    grid.paste(self.border)
    draw = ImageDraw.Draw(grid)
    draw.line((0, 0, 500, 0), fill='green', width=10)
    for row in range(5):
      start = row * 5
      end = start + 5
      y = border_margin + ((row + 1) * tile_padding) + (row * tile_size)
      for idx, tile in enumerate(self.tiles[start:end]):
        x = border_margin + ((idx + 1) * tile_padding) + (idx * tile_size)
        grid.paste(tile.image, (x, y))
    grid.save(out_path)

class BlueKeyGrid(KeyGrid):
  def __init__(self, tiles: List):
    super().__init__(Image.open(blue_border_path, 'r'), tiles)

class RedKeyGrid(KeyGrid):
  def __init__(self, tiles: List):
    super().__init__(Image.open(red_border_path, 'r'), tiles)

def make_red_grid() -> KeyGrid:
  tiles = base_tiles + [Tile(TileType.RED, red) for _ in range(9)] + [Tile(TileType.BLUE, blue) for _ in range(8)]
  random.shuffle(tiles)
  return RedKeyGrid(tiles)

def make_blue_grid() -> KeyGrid:
  tiles = base_tiles + [Tile(TileType.RED, red) for _ in range(8)] + [Tile(TileType.BLUE, blue) for _ in range(9)]
  random.shuffle(tiles)
  return BlueKeyGrid(tiles)

def load_keygrid(idx) -> KeyGrid:
  file_name = f'{generated_path}{idx}.pickle'
  with open(file_name, 'rb') as f:
    return pickle.load(f)

def main():
  for idx in range(40):
    if random.randint(0, 1):
      grid = make_blue_grid()
    else:
      grid = make_red_grid()
    file_name = f'{generated_path}{idx}'
    grid.draw(f'{file_name}.png')
    with open(f'{file_name}.pickle', 'wb') as f:
      pickle.dump(grid, f)

if __name__== "__main__":
  main()