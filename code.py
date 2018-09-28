from PIL import ImageGrab
import os
import time
import win32api, win32con

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

food_coordinates = {
    "shrimp": (42, 332),
    "rice": (84, 332),
    "nori": (42, 382),
    "roe": (84, 382),
    "salmon": (42, 432),
    "unagi": (84, 432)
}

sushi_items = {
    'onigiri': ['rice','rice','nori'],
    'caliroll': ['rice', 'nori', 'roe'],
    'gunkan': ['rice','nori','roe','roe'],
    'salmon': ['rice', 'nori', 'salmon', 'salmon']
}

plate_coordinates = [
    (95, 210),
    (195, 210),
    (295, 210),
    (395, 210),
    (495, 210),
    (595, 210)
]

phone_coordinates = {
    'phone': (584, 357),
    'topping_order': (550, 273),
    'rice_order': (550, 295),
    'sake_order': (550, 319)
}

phone_topping_coordinates = {
    'shrimp': (495, 218),
    'unagi': (579, 216),
    'nori': (491, 275),
    'fish_egg': (582, 269),
    'salmon': (490, 331),
    'back': (557, 333),
    'phone': (599, 336)
}

buy_rice_coordinates = {
    'rice': (549, 284),
    'back': (551, 332),
    'phone': (587, 337)
}

buy_sake_coordinates = {
    'sake': (541, 273),
    'back': (505, 333),
    'phone': (580, 338)
}

delivery_coordinates = {
    'normal': (489, 288),
    'express': (584, 290),
    'back': (482, 330),
    'phone': (588, 339)
}


def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 479)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\screengrabs\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

# Mouse clicks.
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print("Click.")

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print("Left Down")

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print("Left Release")

# Mouse movement.

def mousePos(coord):
    win32api.SetCursorPos((x_pad + coord[0], y_pad + coord[1]))

def get_coords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x,y)

def clear_tables():
    for coordinate in plate_coordinates:
        mousePos(coordinate)
        leftClick()
    time.sleep(1)

def makeFood(food):
    if food in sushi_items:
        for food_item in sushi_items[food]:
            mousePos(food_coordinates[food_item])
            leftClick()
            time.sleep(.05)
        time.sleep(.1)
        foldMat()
        time.sleep(1.5)

def foldMat():
    mousePos((food_coordinates['roe'][0] + 100, food_coordinates['roe'][1]))
    leftClick()
    time.sleep(.1)

def startGame():
    # location of first menu
    mousePos((300, 207))
    leftClick()
    time.sleep(.1)

    # location of second menu
    mousePos((319, 389))
    leftClick()
    time.sleep(.1)

    # location of third menu
    mousePos((579, 450))
    leftClick()
    time.sleep(.1)

    # location of fourth menu
    mousePos((319, 374))
    leftClick()
    time.sleep(.1)

def main():
    pass

if __name__ == '__main__':
    main()