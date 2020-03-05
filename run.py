import pyautogui
import time


class detector:
    def __init__(self, pos):
        self.name = pos
        self.pixel = None

    def colortell(self, pixel):
        if pixel[0] > 200:
            if pixel[1] < 150:
                print(self.name + ' ' + 'click')

        elif pixel[0] > 100:
            print(self.name + ' ' + 'up')

        elif pixel[0] < 50 and pixel[1]>200:
            print(self.name + ' ' + 'hold')

        else:
            if pixel[1] > 170:
                print(self.name + ' ' + 'left')
            elif pixel[1] > 100:
                print(self.name + ' ' + 'right')

    def check(self, position):
        while True:
            self.pixel = pyautogui.screenshot().getpixel(position)
            self.colortell(self.pixel)
            time.sleep(0.01)




