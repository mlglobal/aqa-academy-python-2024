from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BaseApp:

    def __init__(self, browser) -> None:
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def wait_and_click(self, locator, timeout=15):
        # read what is implicit and explisit waiters
        elem = self.browser.find_element(By.XPATH, locator)
        elem.click()   
    
    def enter_text(self, locator, text):
        elem = self.browser.find_element(By.XPATH, locator)
        elem.clear()
        elem.send_keys(text)

    def change_to_text(self, locator):
        elem = self.browser.find_element(By.XPATH, locator)
        return elem.text
        
    def close_browser(self):
        self.browser.close()       
    