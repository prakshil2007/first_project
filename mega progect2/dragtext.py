import pyautogui
import time
import pyperclip

pyautogui.click(1294, 1166)
time.sleep(1)

pyautogui.moveTo(555, 120)
pyautogui.dragTo(1877, 1030, duration=1.0, button='left')

pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

text = pyperclip.paste()

print(text)