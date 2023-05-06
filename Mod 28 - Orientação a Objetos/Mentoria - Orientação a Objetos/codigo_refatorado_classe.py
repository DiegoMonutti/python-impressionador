#Refatorando o código para Orientação a Objetos - Classes:
import pyautogui
import pyperclip
import time

class MeuRobo():

    def __init__(self, tempo_espera):
        self.tempo_espera = tempo_espera
        pyautogui.PAUSE = 1
    
    def abrir_programa(self, nome_programa):
        pyautogui.press('win')
        pyautogui.write(nome_programa)
        pyautogui.press('enter')
    
    def digitar_enter(self, texto):
        pyperclip.copy(texto)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
    
    def aguardar(self):
        time.sleep(self.tempo_espera)
    
    def digitar_aguardar(self, texto):
        self.digitar_enter(texto)
        self.aguardar()

    def clicar(self, x, y, botao='left'):
        pyautogui.click(x, y, button=botao)
    
    def pegar_posicao_mouse(self):
        for i in range(5):
            print(f'Pegando a posição em {5 - i} segundos')
            time.sleep(1)
        print(pyautogui.position())
    
    def extrair_link(self, x, y):
        self.clicar(x, y, botao='right')
        pyautogui.press('up')
        pyautogui.press('up')
        pyautogui.press('enter')
        texto = pyperclip.paste()
        print(texto)