# firstly install : pip install pyautogui
import pyautogui
import time
while True:
    time.sleep(1)
    pyautogui.typewrite("How are you?")
    time.sleep(1)
    pyautogui.press("enter")

