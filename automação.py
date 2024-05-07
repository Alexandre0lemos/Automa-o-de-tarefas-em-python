import pyautogui
import pandas
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(3)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(2)

pyautogui.click(548, 375)
pyautogui.write('nomedogmail@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345678')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(2)

lista = pandas.read_csv('produtos.csv')

for x in lista.index:
    pyautogui.click(484, 258)
    pyautogui.write(str(lista.loc[x, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[x, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[x, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[x, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[x, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(lista.loc[x, 'custo']))
    pyautogui.press('tab')
    obs = str(lista.loc[x, 'obs'])
    if obs != 'nan':
        pyautogui.write(str(lista.loc[x, 'obs']))
        pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('pageup')