from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

#  ---------- EDIT ---------- 
mail_address = 'email\n' # replace email
password = 'passsword\n' # replace password
#  ---------- EDIT ---------- 
wait = WebDriverWait(driver, 20)
driver = uc.Chrome(use_subprocess=True)
url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&continue=https://myaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button'
driver.get(url)


wait.until(EC.visibility_of_element_located(By.NAME, 'identifier').send_keys(mail_address))
sleep(2)
wait.until(EC.visibility_of_element_located(By.NAME, 'password').send_keys(password))
print("You're in!! enjoy")


# [ ---------- paste your code here ---------- ]
