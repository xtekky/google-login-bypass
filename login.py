import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main:
  def __init_(self) -> None:
    self.url    = 'https://accounts.google.com/ServiceLogin'
    self.driver = driver = uc.Chrome(use_subprocess=True)
    self.time   = 10
    
  def login(self, email, password):
    WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
    WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(f'{password}\n')
                                                                                
    self.code()
                                                                                  
  def code(self):
    # [ ---------- paste your code here ---------- ]
    time.sleep(self.time)                                                                                  
                                                                                  
if __name__ == "__main__":
  #  ---------- EDIT ----------
  email = 'email' # replace email
  password = 'password' # replace password
  #  ---------- EDIT ----------                                                                                                                                                         
 
  driver = Main()
  driver.login(email, password)                                                                                
