import time 
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOOGLE_KEY = KeyCode(char="t") # <== altere pra tecla de preferencia dentro de char="". A tecla dentro de char="" irá começar o autoclick

clicking = False

mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01)


def toogle_event(key):
    if key == TOOGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toogle_event) as listener:
    listener.join()