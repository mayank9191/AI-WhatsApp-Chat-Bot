import pyautogui
import time


def annoy():

    pyautogui.click(466, 695)
    time.sleep(0.7)
    pyautogui.click(316, 308)
    pyautogui.typewrite("cow")
    time.sleep(0.7)
    pyautogui.click(264, 356)
    pyautogui.press("enter")
    time.sleep(0.7)


for i in range(5):
    annoy()
