from appJar import gui
# import pprint
# pp = pprint.PrettyPrinter(indent=2)

def build_on_click_word(word_card_name, label_name, person_card_name):
  return lambda e: [app.removeImage(word_card_name), \
                    app.showImage(person_card_name), \
                    app.removeLabel(label_name)]

def get_image_widget(name):
  return app.widgetManager.get(10, name)

while True:
  red_spymaster = input('Who will be red spymaster? ')
  blue_spymaster = input('Who will be blue spymaster? ')
  print('Building game board...')
  app = gui('Monikers')
  app.setImageLocation('game-board/resources')

  app.startFrame("BLUE_GUTTER", row=0, column=0)
  for idx in range(9):
    name = f'blue-gal{idx}'
    app.addImage(name, 'blue-gal.png')
    app.zoomImage(name, -2)
  app.stopFrame()

  app.startFrame("BOARD", row=0, column=1)
  for row in range(5):
    for col in range(5):
      id = f'{row}{col}'
      word_card_name = f'word-card{id}'
      person_card_name = f'person-card{id}'
      label_name = f'word{id}'
      app.addImage(word_card_name, 'word-card.png', row, col)
      app.addImage(person_card_name, 'blue-gal.png', row, col)
      app.hideImage(person_card_name)
      app.setStretch('both')
      app.setSticky('')
      app.addLabel(label_name, 'SOMETHING', row, col) \
        .bind("<ButtonRelease-1>", build_on_click_word(word_card_name, label_name, person_card_name))
      app.setLabelBg(label_name, 'white')
      app.setLabelFont({ 'size': 20, 'weight': 'bold' }, 'Calibri')
      get_image_widget(word_card_name).bind("<ButtonRelease-1>", \
                                            build_on_click_word(word_card_name, label_name, person_card_name))
  app.stopFrame()

  app.startFrame("RED_GUTTER", row=0, column=2)
  for idx in range(8):
    app.addImage(f'red-dude{idx}', 'red-dude.png')
    app.zoomImage(f'red-dude{idx}', -2)
  app.stopFrame()
  #pp.pprint(app.widgetManager.widgets)

  app.go()