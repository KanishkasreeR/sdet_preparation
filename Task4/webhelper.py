from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebElementHelper:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  

    def find_element(self, by, value):
        try:
            element = self.wait.until(EC.presence_of_element_located((by, value)))
            return element
        except:
            print("Element not found.")
            return None


    def click_element(self, by, value):
        try:
            element = self.wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
        except:
            print("Could not click the element.")

    def enter_text(self, by, value, text):
        try:
            element = self.find_element(by, value)
            if element:
                element.clear()  
                element.send_keys(text)  
        except:
            print("Could not enter text.")
