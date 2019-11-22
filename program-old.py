from selenium import webdriver
from selenium.webdriver.common.keys import Keys

default_username = 'sql_fun_0'
default_password = 'kolo007'

class Follower:

     def __init__(self):
         print("@follower")
         driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
         self.driver = driver.get('https://www.instagram.com')
         # assert 'Follower App' in self.driver.title
         self.authenticate()

     def grab_credentials(self, username, password):
         if not username:
             self._username = default_username
         if not password:
             self._password = default_password

     def authenticate(self):
         username_field = self.driver.find_element_by_name('username')
         password_field = self.driver.find_element_by_name('password')
         print(username_field)
         print(password_field)

         if not username_field or not password_field:
             print('Required body fields not found')
             pass

         else:
             self.grab_credentials('', '')
             print('Authenticate with credentials: ' + self._username + ':' + self._password)
             username_field.send_keys(self._username)
             password_field.send_keys(self._password)


follower = Follower()
