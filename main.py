from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np

#open image
image = Image.open("waianae.jpg")

#open the photo viewer
image.show()
plt.imshow(image)

#text Watermark
watermark_image = image.copy()
draw = ImageDraw.Draw(watermark_image)

w, h = image.size
#(font type, font size)
x, y = int(w / 2), int(h / 2)
if x > y:
    font_size = y
elif y > x:
    font_size = x
else:
    font_size = x

font = ImageFont.truetype("arial.ttf", int(font_size / 6))

#add watermark
#(255,255,255) - White color text
draw.text((x, y), "Waianae", fill=(255, 255, 255), font=font, anchor='ms')
plt.subplots(1, 2)
plt.title("white text")
plt.imshow(watermark_image)

watermark_image.show()

