import pyautogui, webbrowser
from time import sleep
webbrowser.open('https://web.whatsapp.com/send?phone=+57')
sleep(60)
pyautogui.press('enter')

for i in range(400):
    pyautogui.typewrite(f'{i}. sapa')
    pyautogui.press('enter')

    
