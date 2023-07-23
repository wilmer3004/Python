import pyautogui, webbrowser
from time import sleep
webbrowser.open('https://web.whatsapp.com/send?phone=+573223969114')
sleep(20)
pyautogui.typewrite('Escribí un programa unicamente para decirte lo mucho que te quiero: ')
pyautogui.press('enter')

for i in range(11):
    pyautogui.typewrite(f'{i}. TQM <3')
    pyautogui.press('enter')

pyautogui.typewrite(f'Eres Hermosa <3')
pyautogui.press('enter')
    