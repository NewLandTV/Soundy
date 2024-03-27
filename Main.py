import numpy as np
import winsound as sound
from PIL import Image

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_WHITE = (255, 255, 255)

name = input()
image = Image.open(f"Images/{name}.png")
pixel = np.array(image)

for i in range(int((pixel.size / 3) ** (0.5))):
    for j in range(int(pixel[i].size / 3)):
        frequency = 0
        
        if (pixel[i][j] == COLOR_BLACK).all():
            frequency = 44
        elif (pixel[i][j] == COLOR_RED).all():
            frequency = 768
        elif (pixel[i][j] == COLOR_GREEN).all():
            frequency = 384
        elif (pixel[i][j] == COLOR_BLUE).all():
            frequency = 987
        elif (pixel[i][j] == COLOR_WHITE).all():
            frequency = 1001

        sound.Beep(frequency, 250)
