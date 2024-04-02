import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager



class WindowHandleClass:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))





   # browser initiation and url navigation
   def initiation_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : URL is incorrect/Network Error")
           return False


   # Quit browser
   def shutdown(self):
       if self.initiation_function():
           return self.driver.quit()
       else:
           return False

   # To fetch current url
   def fetch_url(self):
       if self.initiation_function():
           return self.driver.current_url
       else:
           return False

   # To open FAQ link(anchor tag element) in new window
   def open_FAQ_in_new_window(self):
       if self.initiation_function():
           faq_link_element = self.driver.find_element('link text', 'FAQ')
           faq_link_element.click()
           time.sleep(5)
       else:
           return False

   # To open Partners link(anchor tag element) in new window
   def open_partners_in_new_window(self):
       if self.initiation_function():
           partners_link_element = self.driver.find_element('link text', 'PARTNERS')
           partners_link_element.click()
           time.sleep(5)
       else:
           return False

   # To display window handle / frame id's of windows
   def display_window_handles(self):
       if self.initiation_function():
           faq_window_handle = self.driver.window_handles[1]
           self.driver.switch_to.window(faq_window_handle)
           time.sleep(5)
           current_window_name = self.driver.current_window_handle
           print("FAQ page window name:", current_window_name)
           partners_window_handle = self.driver.window_handles[2]
           self.driver.switch_to.window(partners_window_handle)
           time.sleep(5)
           current_window_name = self.driver.current_window_handle
           print("Partners page window name:", current_window_name)
           time.sleep(5)
           print("Opened Windows / Frame ID's:", self.driver.window_handles)
       else:
           return False


   # To close FAQ and Partners window and switch to main window(Cowin Home)
   def close_window_handles(self):
       main_window_handle = self.driver.window_handles[0]
       faq_window_handle = self.driver.window_handles[1]
       self.driver.close()
       time.sleep(5)
       self.driver.switch_to.window(faq_window_handle)
       time.sleep(5)
       self.driver.close()
       time.sleep(5)
       self.driver.switch_to.window(main_window_handle)
       print("Home page title:", self.driver.title)


