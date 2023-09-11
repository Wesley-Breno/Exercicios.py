from selenium import webdriver  # Chamando o driver para usar na web
from selenium.webdriver.common.by import By  # Achar tag com base no class_name, name, id e etc. Pra poder interagir.
from time import sleep  # Funcao sleep para fazer o programa esperar para a pagina poder carregar

driver = webdriver.Chrome()  # Informando que vai usar o chrome e chamando as funcoes
driver.get('https://github.com/')  # Entrando no site

driver.find_element(By.XPATH, '/html/body/div[1]/header/div'
                              '/div[2]/div[2]/div[2]/a').click()  # Achando tag pelo XPATH e clicando.
sleep(1)  # Esperando a pagina carregar por 1 segundo

driver.find_element(By.NAME, 'login').send_keys('Aqui ficaria o email')  # Tag onde fica o email e colocando o email
driver.find_element(By.NAME, 'password').send_keys('Aqui ficaria a senha')  # Indo na tag onde fica a senha e colocando a senha
driver.find_element(By.NAME, 'commit').click()  # Clicando na tag para logar

sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/header/div[7]/details/summary/img').click()  # Clicando no menu do perfil
sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/header/div[7]/details/details-menu/form/button').click()  # Clicando em sair

