import pyautogui
import time

msg = ['hello', '''Lortware like Aldus PageMaker including versions of Lorem''']
time.sleep(5)
for i in range(100):
    pyautogui.typewrite(msg[i%len(msg)])
    pyautogui.typewrite("\n")
