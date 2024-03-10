import pyautogui
from pynput.keyboard import Key, Listener
import random
from win32 import win32api
import win32con
import sys
from threading import Thread
import time

pressed=False                                         

class click(Thread):

    global pressed
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
     
    def run(self):
        while (pressed):

                randomint=random.uniform(0.2,0.4)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                randomstart=random.uniform(0.0,0.2)
                time.sleep(randomint)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                time.sleep(randomstart)
        
                time.sleep(0.1);


def on_press(key):
    try:
        key_press = key.char
        global pressed
        print("PRESSED", key_press)
    
        if key_press == "w":
            print(pressed)
            if(pressed):
                    pressed=False
                    #sys.exit()
                    print('trigger')
            else:
                    pressed=True
                    click()
    except AttributeError:
        print('error')
with Listener(on_press=on_press) as listener:
    listener.join()
