from appJar import gui
from word_list import get_word_set
from keycard_generator import BlueKeyGrid, RedKeyGrid, Tile, TileType, load_keygrid
from comms import send_mms

game_number = 0
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

def pick_spymaster(team):
  team = team.lower()
  while True:
    spymaster = input(f'What is the phone number of the {team.title()} Spymaster? ')
    msg = f'You are the Spymaster for the {team.title()} team! Give one word clues to help your team guess the {team} words. Careful to avoid the \'X\' word!'
    keygrid_url = f'https://raw.githubusercontent.com/marve/monikers/master/game-board/resources/generated/grid-{game_number}.png'
    try:
      send_mms(spymaster, msg, keygrid_url)
      if input(f'Did the {team.title()} Spymaster get the message? ').lower()[:1] == 'y':
        break
    except Exception as e: print(e)
    print('Let\'s try again')

while True:
  print(f'Setting up game {game_number}')
  words = get_word_set(game_number)
  keygrid = load_keygrid(game_number)
  pick_spymaster('red')
  pick_spymaster('blue')

  app = gui('Monikers')
  app.setLogLevel('ERROR')
  app.setImageLocation('game-board/resources')

  app.startFrame("BLUE_GUTTER", row=0, column=0)
  num_blue_cards = 9 if type(keygrid) is BlueKeyGrid else 8
  blue_cards = []
  for idx in range(num_blue_cards):
    name = f'blue-gal{idx}'
    app.addImage(name, 'blue-gal.png')
    blue_cards.append(get_image_widget(name))
    app.zoomImage(name, -2)
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
    name = f'red-dude{idx}'
    app.addImage(name, 'red-dude.png')
    red_cards.append(get_image_widget(name))
    app.zoomImage(name, -2)
  app.stopFrame()

  app.go()
  game_number = game_number + 1
