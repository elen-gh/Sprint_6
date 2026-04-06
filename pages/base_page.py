from allure import step
from src.config import Config
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    TIMEOUT = Config.TIMEOUT 
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator, timeout=TIMEOUT):
        with step(f"Find element {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        
    def click_element(self, locator, timeout=10):
        with step(f"Click to {locator}"):
            button = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", button)        
    
    def click_nativ_element(self, locator, timeout=10):
        with step(f"Click to {locator}"):
            element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            element.click() 

    def enter_text(self, locator, text, timeout=10):
        with step(f"Fill text {text} into field with locator {locator}"):
            field = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", field) 
            field.send_keys(text)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def element_is_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def accept_cookies(self):
        cookie_button = (By.ID, "rcc-confirm-button")
        if self.element_is_present(cookie_button):
            self.click_element(cookie_button)

    def wait_for_url_contains(self, url_part, timeout=10):
        with step(f"Wait for URL: {url_part}"):
            return WebDriverWait(self.driver, timeout).until(lambda driver: url_part in driver.current_url)