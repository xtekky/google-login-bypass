import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  ---------- EDIT ----------
email = 'email\n' # replace email
password = 'password\n' # replace password
#  ---------- EDIT ----------

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)

driver.get('https://accounts.google.com/ServiceLogin')


wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
print("You're in!! enjoy")
sleep(10)

# [ ---------- paste your code here ---------- ]


