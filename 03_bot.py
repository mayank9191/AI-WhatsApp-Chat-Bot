import pyautogui
import time
import pyperclip
import _02_AI


def click_and_drag_select():
    # Step 1: Click on the icon at (905, 743)
    pyautogui.click(993, 743)
    time.sleep(0.5)  # Give a short delay to ensure the click action completes

    # Step 2: Drag from (446, 116) to (1350, 649) to select text
    # pyautogui.moveTo(473, 181)
    pyautogui.moveTo(524, 408)
    # pyautogui.dragTo(719, 716, duration=4)  # Drag over 1 second
    pyautogui.dragTo(897, 667, duration=2)  # Drag over 1 second

    # Step 3: Press 'Ctrl+C' to copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')

    # pyautogui.click(913, 348)
    pyautogui.click(819, 419)
    time.sleep(1)  # Give a short delay to ensure the copy action completes

    # Step 4: Get the text from the clipboard and store it in a variable
    copied_text = pyperclip.paste()
    print(copied_text)
    return copied_text


a = click_and_drag_select()
c = _02_AI.aiProcess(a)
pyautogui.click(633, 697)
pyautogui.typewrite(c)
time.sleep(0.5)
# pyautogui.press("enter")
