from appJar import gui
from word_list import get_word_set
from keycard_generator import BlueKeyGrid, RedKeyGrid, Tile, TileType, load_keygrid, max_grids
from comms import send_mms
import os, random

game_number = 1
grid_numbers = list(range(max_grids))
random.shuffle(grid_numbers)
blue_cards = []
red_cards = []

def build_on_click_word(word_card_name, label_name, person_card_name, pop_fn):
  return lambda e: [app.removeImage(word_card_name), \
                    app.showImage(person_card_name), \
                    app.removeLabel(label_name), \
                    pop_fn()]

def get_image_widget(name):
  return app.widgetManager.get(10, name)

def pop_red():
  red_cards.pop().grid_remove()

def pop_blue():
  blue_cards.pop().grid_remove()

def pop_none():
  pass

def toggle_blue_gender(e):
  toggle_gender('blue')

def toggle_red_gender(e):
  toggle_gender('red')

def toggle_gender(color):
  images = app.widgetManager.group(10, None)
  for key in images.keys():
    image_path = os.path.basename(images[key].image.path)
    if color in image_path:
      if 'gal' in image_path:
        app.setImage(key, f'{color}-dude.png')
      else:
        app.setImage(key, f'{color}-gal.png')
      if key.startswith(color):
        app.zoomImage(key, -2)

def pick_spymaster(team, keygrid_url):
  team = team.lower()
  while True:
    spymaster = input(f'What is the phone number of the {team.title()} Spymaster? ')
    msg = f'You are the Spymaster for the {team.title()} team! Give one-word clues to help your team guess the {team} words. Careful to avoid the \'X\' word!'
    try:
      send_mms(spymaster, msg, keygrid_url)
      if input(f'Did the {team.title()} Spymaster get the message? ').lower()[:1] == 'y':
        break
    except Exception as e: print(e)
    print('Let\'s try again')

while True:
  words = get_word_set(game_number)
  grid_number = grid_numbers.pop()
  keygrid_url = f'https://raw.githubusercontent.com/marve/monikers/master/resources/generated/grid-{grid_number}.png'
  print(f'Setting up game {game_number}')# using {keygrid_url}')
  keygrid = load_keygrid(grid_number)
  pick_spymaster('red', keygrid_url)
  pick_spymaster('blue', keygrid_url)

  app = gui('Monikers')
  app.setLogLevel('ERROR')
  app.setFullscreen()
  app.setImageLocation('resources')

  app.startFrame("BLUE_GUTTER", row=0, column=0)
  num_blue_cards = 9 if type(keygrid) is BlueKeyGrid else 8
  blue_cards = []
  for idx in range(num_blue_cards):
    name = f'blue{idx}'
    app.addImage(name, 'blue-gal.png')
    blue_cards.append(get_image_widget(name))
    app.zoomImage(name, -2)
    get_image_widget(name).bind('<ButtonRelease-1>', toggle_blue_gender)
  app.stopFrame()

  app.startFrame("BOARD", row=0, column=1)
  for row in range(5):
    for col in range(5):
      id = (5 * row) + col
      tile = keygrid.tiles[id]
      word_card_name = f'word-card{id}'
      person_card_name = f'person-card{id}'
      label_name = f'word{id}'
      person_card_image = 'blue-gal.png'
      pop_fn = pop_blue
      if tile.tile_type == TileType.RED:
        person_card_image = 'red-dude.png'
        pop_fn = pop_red
      elif tile.tile_type == TileType.NEUTRAL:
        person_card_image = 'neutral-dude.png'
        pop_fn = pop_none
      elif tile.tile_type == TileType.ASSASSIN:
        person_card_image = 'assassin_card.png'
        pop_fn = pop_none
      app.addImage(word_card_name, 'word-card.png', row, col)
      app.addImage(person_card_name, person_card_image, row, col)
      app.hideImage(person_card_name)
      app.setStretch('both')
      app.setSticky('')
      click_word_fn = build_on_click_word(word_card_name, label_name, person_card_name, pop_fn)
      app.addLabel(label_name, words.pop(), row, col) \
        .bind("<ButtonRelease-1>", click_word_fn)
      app.setLabelBg(label_name, 'white')
      app.setLabelFont({ 'size': 20, 'weight': 'bold' }, 'Calibri')
      get_image_widget(word_card_name).bind("<ButtonRelease-1>", click_word_fn)
  app.stopFrame()

  app.startFrame("RED_GUTTER", row=0, column=2)
  red_cards = []
  num_red_cards = 9 if type(keygrid) is RedKeyGrid else 8
  for idx in range(num_red_cards):
    name = f'red{idx}'
    app.addImage(name, 'red-dude.png')
    red_cards.append(get_image_widget(name))
    app.zoomImage(name, -2)
    get_image_widget(name).bind('<ButtonRelease-1>', toggle_red_gender)
  app.stopFrame()

  app.go()
  game_number = game_number + 1
