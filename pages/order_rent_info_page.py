from pages.base_page import BasePage 
from selenium.webdriver.common.by import By
from allure import step
from locators.order_rent_info_page_locators import OrderRentInfoPageLocators
from selenium.webdriver.common.keys import Keys

class OrderRentInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
   
    def fill_order_rent_info(self, date, period, comment="", color="", **kwargs):

        with step(f"Enter date: {date}"): 
            self.enter_text(OrderRentInfoPageLocators.DATE_FIELD, date)
            self.find_element(OrderRentInfoPageLocators.DATE_FIELD).send_keys(Keys.ENTER)
            
        with step(f"Enter period: {period}"):
            self.click_nativ_element(OrderRentInfoPageLocators.PERIOD_FIELD)
            period_locator = By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']"
            self.click_nativ_element(period_locator)

        with step(f"Select color: {color}"):
            if color: self.click_nativ_element((By.XPATH, f"//label"))

        with step(f"Enter comment: {comment}"):
            self.enter_text(OrderRentInfoPageLocators.COMMENT_FIELD, comment)

    @step("Click LAST_ORDER_BUTTON")
    def last_order_button_click(self):
        self.click_element(OrderRentInfoPageLocators.LAST_ORDER_BUTTON)
        