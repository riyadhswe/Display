import pyautogui
import time
import numpy
import keyboard
import win32api ,win32con
time.sleep(2)

while keyboard.is_pressed('q') == False:
    H = pyautogui.locateOnScreen('img_2.png',grayscale = True,confidence=.8)
    pyautogui.click(H)
    if H != None:
        print("i see it")
    else:
        print("Not found")





