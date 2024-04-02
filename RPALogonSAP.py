import pyautogui
import time

pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('SAP')
pyautogui.press('enter')
pyautogui.PAUSE = 4
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('FCONTO')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("su01")
pyautogui.press('enter')
#COPY USER
pyautogui.write('JSILVA')
pyautogui.hotkey('shift', 'f5')
#NEWUSER
pyautogui.write('GSOUZA')
pyautogui.press('down')
pyautogui.press('space')
pyautogui.press('f5')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('Mudar123@')
pyautogui.press('tab')
pyautogui.write('Mudar123@')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'left')
pyautogui.hotkey('ctrl', 'left')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.PAUSE = 2
pyautogui.press('down')
pyautogui.hotkey('ctrl', 'a')
#Sobrenome do novo usuario
pyautogui.write('SOUZA SANTOS')
pyautogui.press('tab')
#Nome do novo usuario
pyautogui.write('JOSE')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
#Cargo
pyautogui.write('CONSULTOR VENDAS SR')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
#matricula
pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
#e-mail
pyautogui.write('jose.souza@empresa.com.br')
pyautogui.hotkey('ctrl', 's')
pyautogui.PAUSE = 2
pyautogui.press('enter')
time.sleep(2)

pyautogui.alert("O código acabou de rodar. Pode usar o seu computador de novo")