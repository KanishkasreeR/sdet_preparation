from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "j_username")
    PASSWORD = (By.NAME, "j_password")
    LOGIN = (By.XPATH, "//input[@type='submit']")
    ERROR_MESSAGE = (By.ID, "errorMsg") 
    DASHBOARD_HEADER = (By.ID, "https://skillrack.com/faces/ui/profile.xhtml")  

    def enter_username(self, username):
        self.enter_text(*self.USERNAME, text=username)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD, text=password)

    def click_login(self):
        self.click(*self.LOGIN)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

    def is_login_failed(self):
        return self.is_displayed(*self.ERROR_MESSAGE)

    def is_login_successful(self):
        return self.is_displayed(*self.DASHBOARD_HEADER)

    def is_on_login_page(self):
        return "login" in self.driver.current_url or "profile.xhtml" in self.driver.current_url
