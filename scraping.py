#IMPORTANDO BIBLIOTECAS
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#ENTRADA DE DADOS
tag = str(input('Digite uma palavra de Pesquisa\n'))

#CONFIGURANDO DRIVER
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options = chrome_options)

#ENTRANDO NO SITE
URL = f'https://www.sp-arte.com/arquivo/?q={tag}'
driver.get(URL)

TIMESLEEP = 0.1

#ROLANDO ATÉ O RODAPÉ DA PÁGINA
rodape_pagina = driver.execute_script("return document.body.scrollHeight")

while True:
    #ROLANDO ATÉ A 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #ESPERANDO CARREGAR A PÁGINA
    time.sleep(TIMESLEEP)

    # CALCULANDO A ALTURA DA PÁGINA ANTERIOR ROLADA COM A NOVA
    nova_altura = driver.execute_script("return document.body.scrollHeight")
    if nova_altura == rodape_pagina:
        break
    rodape_pagina = nova_altura

#CAPTURANDO CONTEÚDO
conteudo = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div/div')

#ORGANIZANDO OBRAS
obras = []
for i in range(len(conteudo)):
    obra = conteudo[i].text
    obra = obra.split('\n')
    obras.append(obra)

#EXTRAINDO OBRAS
obras = pd.DataFrame(obras)
obras.to_excel('Obras.xlsx')

#FECHANDO NAVEGADOR
driver.quit()
