from PIL import ImageGrab
import os
import time

"""
All coordinates assume a screen resolution of 1366 x 768, and Chrome
maximized with the new version.
No key presses.
x_pad = 187
y_pad = 345
Play area = x_pad + 1, y_pad + 1, 827, 702
"""

# Globals
# ---------------

x_pad = 187
y_pad = 222

def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 479)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\screengrabs\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()