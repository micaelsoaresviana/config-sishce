import pyautogui
import time
pyautogui.press("win")
time.sleep(2)
pyautogui.keyDown("shift")
pyautogui.write("/")
pyautogui.keyUp("shift")

