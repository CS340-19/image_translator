import sys
from PIL import Image

img = Image.open(sys.argv[1])
img.show()

print(img.format)

print(img.mode)

