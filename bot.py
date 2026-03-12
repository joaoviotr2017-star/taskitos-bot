from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

RA = "0001125909067sp"
SENHA = "djanira9B@"

def executar():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://taskitos.cupiditys.lol")

    time.sleep(5)

    # preencher RA
    driver.find_element(By.NAME, "ra").send_keys(RA)

    # preencher senha
    driver.find_element(By.NAME, "senha").send_keys(SENHA)

    print("Clique na caixa 'Eu não sou um robô' no navegador")

    time.sleep(20)

    # clicar atividades pendentes
    driver.find_element(By.XPATH, "//button[contains(text(),'Atividades Pendentes')]").click()

    time.sleep(5)

    # selecionar todas atividades
    driver.find_element(By.XPATH, "//label[contains(text(),'Selecionar Todas')]").click()

    time.sleep(2)

    # fazer lições
    driver.find_element(By.XPATH, "//button[contains(text(),'Fazer Lições Selecionadas')]").click()

    time.sleep(10)

    driver.quit()


executar()
