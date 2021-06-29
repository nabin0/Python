import webbrowser as wb
import time
import pyautogui

url = "web.whatsapp.com"  # Url of website you want to send message
# Path of browser for windows
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# wb.register('chrome', None,wb.BackgroundBrowser(chrome_path)) #register chrome in case it doesont open
wb.get(chrome_path).open(url)  # Opening browser
time.sleep(10)

# Get input message
# msg = input("Enter the message you want to send.")
msg = "Message here"  # Hardcoding var value for test purpose
msg = [char for char in msg]

no_of_msg = 10
msg_sent = 0
while msg_sent < no_of_msg :
    for i in range(len(msg)):
        print(msg[i])
        pyautogui.press(msg[i])
    msg_sent += 1
    pyautogui.press("enter")
