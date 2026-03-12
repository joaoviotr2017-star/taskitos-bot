from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def executar():

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://taskitos.cupiditys.lol")

    time.sleep(5)

    driver.find_element(By.XPATH, "//button[contains(text(),'Contas Salvas')]").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//div[contains(text(),'0001125909067sp')]").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'Atividades Pendentes')]").click()

    time.sleep(5)

    driver.find_element(By.XPATH, "//label[contains(text(),'Selecionar Todas')]").click()

    time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'Fazer Lições Selecionadas')]").click()

    time.sleep(10)

    driver.quit()

schedule.every().day.at("18:00").do(executar)

while True:
    schedule.run_pending()
    time.sleep(60)