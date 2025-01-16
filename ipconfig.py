import pyautogui
import time

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("cmd")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("ipconfig")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("ipconfig /release")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("ipconfig /renew")
pyautogui.press("enter")
