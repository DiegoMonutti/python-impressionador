#Importar as bibliotecas:
import time, urllib
from IPython.display import display
from selenium import webdriver 
import pandas as pd 
import numpy as np
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox

#Ler CSV:
root= Tk()
arquivo = tkinter.filedialog.askopenfilename(title = 'Selecione o Arquivo csv com Canais e Keywords')
root.destroy()

buscas_df = pd.read_csv(arquivo, encoding = 'utf-8', sep=';')
display(buscas_df.head())

buscas_canais = buscas_df['Canais'].unique()

#Ler videos de todas as buscas:
driver = webdriver.Chrome() 

#Pegando os itens dos canais:
hrefs = []
for canal in buscas_canais:
    if canal is np.nan:
        break
    hrefs.append(canal)
    driver.get(canal)
    while len (driver.find_elements(By.CLASS_NAME, 'tab-content')) < 1:
        time.sleep(1)
    time.sleep(2)
    tab = driver.find_elements(By.CLASS_NAME, 'tab-content')[1].click()
    time.sleep(5)
    altura = 0
    nova_altura = 1
    while nova_altura > altura:
            altura = driver.execute_script('return document.documentElement.scrollHeight')
            driver.execute_script('window.scrollTo(0, ' + str(altura) + ');')
            time.sleep(3)
            nova_altura = driver.execute_script('return document.documentElement.scrollHeight')
    videos = driver.find_elements(By.ID, 'thumbnail')
    try:
        for video in videos:
            meu_link = video.get_attribute('href')
            if meu_link:
                if not 'googleadservices' in meu_link: 
                    hrefs.append(meu_link)
    except StaleElementReferenceException:
        time.sleep(2)
        videos = driver.find_elements(By.ID, 'thumbnail')
        for video in videos:
            meu_link = video.get_attribute('href')
            if meu_link:
                if not 'googleadservices' in meu_link: 
                    hrefs.append(meu_link)
    print(f'Pegamos {len(videos)} vídeos do Canal {canal}')

driver.quit()

#Salvando o resultado em um csv:
hrefs_df = pd.DataFrame(hrefs)
hrefs_df.to_csv(r'Canais Prontos.csv', sep=',', encoding='utf-8')
root= Tk()
messagebox.showinfo('Programa Finalizado com Sucesso', 'Seu arquivo csv foi gerado com sucesso na pasta do Programa')
root.destroy()