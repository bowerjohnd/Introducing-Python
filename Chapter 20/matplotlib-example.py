# interpreter example using matplotlib

import matplotlib.pyplot as plot
import matplotlib.image as image

img = image.imread('oreilly.jpg')
plot.imshow(img)
plot.show()
