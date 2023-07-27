import pyautogui, webbrowser
from time import sleep
open('https://web.whatsapp.com/send?phone=+573026000487')
sleep(40)
pyautogui.typewrite('Escribí un programa unicamente para decirte lo mucho que te quiero: ')
pyautogui.press('enter')

for i in range(400):
    pyautogui.typewrite(f'{i}. sapa')
    pyautogui.press('enter')

    