from appJar import gui
import pprint
pp = pprint.PrettyPrinter(indent=2)

def click_fn(row, col, word_card, person_card):
  return lambda e: print(f'clicked {row},{col} {e}', word_card.grid_remove(), person_card.grid())

def add_image(name, file, row=None, col=0):
  img = app.addImage(name, file, row, col)
  widget = app.widgetManager.get(10, name)
  return widget, img

# Calibri bold 20
app = gui('Monikers')
app.setImageLocation('game-board/resources')

app.startFrame("BLUE_GUTTER", row=0, column=0)
for idx in range(9):
  blue_gal_red, img = add_image(f'blue-gal{idx}', 'blue-gal.png')
  app.zoomImage(f'blue-gal{idx}', -2)
app.stopFrame()

app.startFrame("BOARD", row=0, column=1)
for row in range(5):
  for col in range(5):
    id = f'{row}{col}'
    word_card_name = f'word-card{id}'
    person_card_name = f'person-card{id}'
    word_card, _ = add_image(word_card_name, 'word-card.png', row, col)
    person_card, _ = add_image(person_card_name, 'blue-gal.png', row, col)
    person_card.grid_remove()
    word_card.bind("<ButtonRelease-1>", click_fn(row, col, word_card, person_card))
    app.setStretch('both')
    app.setSticky('')
    app.addLabel(f'word{id}', 'SOMETHING', row, col)
    #app.hideLabel(f'word{id}')
    #app.hideImage(word_card_name)
    app.setLabelBg(f'word{id}', 'white')
    app.setLabelFont({ 'size': 20, 'weight': 'bold' }, 'Calibri')
app.stopFrame()

app.startFrame("RED_GUTTER", row=0, column=2)
for idx in range(8):
  blue_gal_red, img = add_image(f'red-dude{idx}', 'red-dude.png')
  app.zoomImage(f'red-dude{idx}', -2)
app.stopFrame()
#pp.pprint(app.widgetManager.widgets)

app.go()