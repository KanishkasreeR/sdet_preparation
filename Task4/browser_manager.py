from selenium import webdriver
import time

class BrowserManager:
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window() 
            self.driver.implicitly_wait(10)  
        except Exception as e:
            print("Something went wrong while opening the browser:", e)
            self.driver = None

    def navigate_to(self, url):
        if self.driver:
            try:
                self.driver.get(url)  
            except Exception as e:
                print("Error loading the URL:", e)

    def quit_browser(self):
        if self.driver:
            time.sleep(2) 
            self.driver.quit() 
