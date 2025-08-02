import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Task5.pages.login_page import LoginPage
from selenium import webdriver

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://skillrack.com/faces/ui/profile.xhtml;jsessionid=9723B3E1273CF9B77F23F71AB9FFBA19")
    
    login_page = LoginPage(driver)
    login_page.login("22cs073@sece", "poorani05")

    assert login_page.is_displayed(*LoginPage.LOGIN) == False

    driver.quit()
