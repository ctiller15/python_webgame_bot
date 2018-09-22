from PIL import ImageGrab
import os
import time

def screenGrab():
    box = (188, 223, 827, 702)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\screengrabs\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def main():
    screenGrab()

if __name__ == '__main__':
    main()