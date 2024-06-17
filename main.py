import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r'C:\Users\Mateo\PycharmProjects\SuiteAutomation-QA\SeleniumDrivers'

driver = webdriver.Chrome()
driver.get('https://frontend-training-taupe.vercel.app/login')

driver.implicitly_wait(5) #Espera COMO MUCHO 3 secs

usernameInput = driver.find_element(By.CSS_SELECTOR, 'input[type="text"][aria-label="Username"]')
usernameInput.send_keys('usuario')

passwordInput = driver.find_element(By.CSS_SELECTOR, 'input[type="password"][aria-label="Password"]')
passwordInput.send_keys('12345Aa!1')

loginButton = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
loginButton.click()
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div/form/label[1]'))
    )

    assert True
    print('true')
except:
    print('feka')

