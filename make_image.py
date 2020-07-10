from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("COOPBL.TTF",14)
img = Image.new('RGB', (200, 100), 'orange')
d = ImageDraw.Draw(img)
d.text((20, 20), 'Hello ' + '\n' + 'World', fill=('blue'), font = font)
img.save('/Users/Neal/Documents/Raingauge/t2i.png')
