# Image to ASCII converter
# python3 imgascii.py logo.png

import sys
from PIL import Image

# get path from command line
imagePath = sys.argv[1]
img = Image.open(imagePath)

# resize the image
width, height = img.size
aspectRatio = height/width
newWidth = 64
newHeight = aspectRatio * newWidth * 0.55
img = img.resize((newWidth, int(newHeight)))

# Convert image to gray scale
img = img.convert('L')
pixels = img.getdata()

# replace each pixel with a character from array
chars = ["S","#","B","&","@","$","%","*",";","!","."]
newPixels = [chars[pixel//25] for pixel in pixels]
newPixels = ''.join(newPixels)

# create image
new_pixels_count = len(newPixels)
ascii_image = [newPixels[index:index + newWidth] for index in range(0, new_pixels_count, newWidth)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

