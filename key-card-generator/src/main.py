from PIL import Image

border = Image.open('key-card-generator/resources/red-border.png', 'r')
blue = Image.open('key-card-generator/resources/blue.png', 'r')

border.paste(blue, (39, 39))
border.save('out.png')