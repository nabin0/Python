import webbrowser as wb
import time
import pyautogui

url = "web.whatsapp.com"
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# wb.register('chrome', None,wb.BackgroundBrowser(chrome_path)) #register chrome in case it doesont open
wb.get(chrome_path).open(url)
time.sleep(15)
while True:
    pyautogui.press("H")
    pyautogui.press("e")
    pyautogui.press("l")
    pyautogui.press("l")
    pyautogui.press("0")
    pyautogui.press("enter")