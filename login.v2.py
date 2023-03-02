# by @Fakesum

from seleniumbase import SB
class Google:
    def __init__(self) -> None:
        self.url    = 'https://accounts.google.com/ServiceLogin'
        self.time   = 10
    
    def login(self, email, password):
        with SB(uc=True) as driver:
                sleep(2)
                driver.type('identifier', f'{email}\n', By.NAME)
                sleep(2)
                driver.type( 'Passwd', f'{password}\n', By.NAME)

                self.code()

    def code(self):
    # [ ---------- paste your code here ---------- ]
        sleep(self.time)
      
 
