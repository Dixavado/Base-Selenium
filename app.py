from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logging

# desabilitar logs do WebDriver
logging.getLogger('selenium').setLevel(logging.ERROR)

# caminho do chromedriver
driver_path = './chromedriver'

# criar um objeto Service
service = Service(executable_path=driver_path)

# criar um objeto de opções
options = webdriver.ChromeOptions()

# adicionar o argumento --disable-blink-features para evitar a detecção do WebDriver
options.add_argument('--disable-blink-features=AutomationControlled')

# criar uma instância do ChromeDriver com as opções de configuração
driver = webdriver.Chrome(service=service, options=options)

# acessar o site do Google
driver.get('https://bot.sannysoft.com')

# manter o navegador aberto
while True:
    pass
