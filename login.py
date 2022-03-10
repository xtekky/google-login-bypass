from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

#  ---------- EDIT ---------- 
mail_address = 'email\n' # replace email
password = 'passsword\n' # replace password
#  ---------- EDIT ---------- 

driver = uc.Chrome(use_subprocess=True)
url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&continue=https://myaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button'
driver.get(url)

driver.find_element(By.NAME, 'identifier').send_keys(mail_address)
sleep(2)
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
print("You're in!! enjoy")


# [ ---------- paste your code here ---------- ]
