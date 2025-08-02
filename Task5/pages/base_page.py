from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element_present(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_for_element_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def click(self, by, value):
        try:
            self.wait_for_element_clickable(by, value).click()
        except Exception as e:
            print(f"Click failed: {e}")

    def enter_text(self, by, value, text):
        try:
            element = self.wait_for_element_present(by, value)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Text entry failed: {e}")

    def get_text(self, by, value):
        try:
            return self.wait_for_element_present(by, value).text
        except Exception as e:
            print(f"Get text failed: {e}")
            return ""

    def is_displayed(self, by, value):
        try:
            return self.wait_for_element_present(by, value).is_displayed()
        except:
            return False
