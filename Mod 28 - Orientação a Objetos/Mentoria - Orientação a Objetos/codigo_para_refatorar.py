import pyautogui
import pyperclip
import time

# abrindo o chrome
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrando no site da hashtag
link = "https://www.hashtagtreinamentos.com/blog"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# aguardar
time.sleep(3)

# clicando no campo de busca
pyautogui.click(x=1157, y=503)

# pesquisando campo de busca
texto = "classe"
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# aguardar
time.sleep(3)

# clicar na imagem
pyautogui.click(x=614, y=535)

# aguardar
time.sleep(3)

# extrair o link
pyautogui.click(x=303, y=646, button="right")
pyautogui.press("up")
pyautogui.press("up")
pyautogui.press("enter")

# printar o texto copiado
texto = pyperclip.paste()
print(texto)

# pegando a posicao de um elemento
for i in range(5):
    print(f"pegando posicao em {5 - i} segundos")
    time.sleep(1)
    
print(pyautogui.position())