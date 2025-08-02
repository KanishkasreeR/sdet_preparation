
from browser_manager import BrowserManager
from webhelper import WebElementHelper
from selenium.webdriver.common.by import By


browser = BrowserManager()
browser.navigate_to("https://skillrack.com/faces/ui/profile.xhtml;jsessionid=9723B3E1273CF9B77F23F71AB9FFBA19")

helper = WebElementHelper(browser.driver)
helper.enter_text(By.NAME, "j_username", "22cs073@sece")
helper.enter_text(By.NAME, "j_password", "poorani05")
helper.click_element(By.XPATH, "//input[@type='submit']")


browser.quit_browser()
