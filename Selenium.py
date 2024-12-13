from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options as OptionsChrome

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time

#Capabilities

caps =  DesiredCapabilities().CHROME

caps['pageLoadStrategy'] = "normal"



#Options

opts = OptionsChrome()

opts.add_argument("disable-inforbar")

opts.add_argument("--disable-extensions")

opts.add_argument("no-sandbox")

opts.add_argument("disable-gpu")

opts.add_argument("lang=es")

opts.add_argument("test-type")

opts.add_argument("force-render-accessibility")

opts.add_argument("disable-extensions")

opts.add_argument("allow-insecure-localhost")

opts.add_argument("ignore-ssl-errors=yes")

opts.add_argument("ignore-certificate-errors")

opts.add_argument("--log-level=3")

opts.add_argument("safebrowsing-disable-download-protection")


#Driver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opts)


#Scenario 1: La aplicacion permita loguear un usuario registrado

# Precondiciones: 

#    - Usuario se encuentre ya registrado.

#

# Pasos: 

#   1. Abrir la web  saucedemo.com   

#   2. Escribir usuario y contraseña (standard_user, secret_sauce)

#   3. Clic en boton Login

#

# Resultado Esperado:

#   - Listado de productos sea visible.



# Paso 1

driver.get("https://www.saucedemo.com")





#Paso 2

#Escribir Usuario

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")



#Escribir Contraseña

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("secret_sauce")


#Paso 3

#Click Boton login

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Login']"))).click()



#Resultado Esperado:

elemento = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH,"//span[text()='Products']")))


time.sleep(10)  # Mantén el navegador abierto por 10 segundos
