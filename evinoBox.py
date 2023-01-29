from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Navegador:
    def __init__(self):
        self.navegador = webdriver.Chrome()
    def acessaSite(self,url):
        self.navegador.get(url)
        self.navegador.maximize_window()

    def login(self,id,email):
       return  self.navegador.find_element(By.NAME,id).send_keys(email,Keys.ENTER)

    def pesquisa(self,palavra):
        pesquisa = self.navegador.find_element(By.NAME, 'search')
        return pesquisa.send_keys(palavra, Keys.ENTER)
    def acharXpath(self,xpath):
        self.navegador.find_element(By.XPATH,xpath).click()
        time.sleep(6)
    def espera(self,tempo):
        return time.sleep(tempo)
    def wait(self):
        wait = WebDriverWait(self.navegador, 40)
        popUp = wait.until(EC.element_to_be_clickable((By.ID, 'onesignal-slidedown-cancel-button')))
        fechar = self.navegador.find_element(By.ID, 'onesignal-slidedown-cancel-button').click()
    def acharClass(self,classe):
        self.navegador.find_element(By.CLASS_NAME, classe).click()


EvinoBox = Navegador()
EvinoBox.acessaSite('https://www.evino.com.br/')
EvinoBox.login('user','luiscampossilva96@gmail.com')
EvinoBox.espera(10)
EvinoBox.pesquisa('Vinho')
EvinoBox.espera(5)
EvinoBox.acharXpath('//*[@id="app"]/div/div[1]/header/div/div/div[1]/div/div[2]/div[2]/div/ul/li[4]/a/span')
EvinoBox.espera(1)
EvinoBox.acharXpath('//*[@id="app"]/div/div[1]/div/div/div/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/div/button')
EvinoBox.wait()
EvinoBox.acharClass('CartNavigation__link')



time.sleep(100000)