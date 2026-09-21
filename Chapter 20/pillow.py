# interpreter example using PIL

from PIL import Image

img = Image.open('oreilly.jpg')
print(img.format)
print(img.size)
print(img.mode)