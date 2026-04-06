from pages.base_page import BasePage 
from selenium.webdriver.common.by import By
from allure import step
from locators.order_person_info_page_locators import OrderPersonInfoPageLocators

class OrderPersonInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_order_person_info(self, name, surname, address, station, phone, **kwargs):
        with step(f"Enter name: {name}"): 
            self.enter_text(OrderPersonInfoPageLocators.NAME_FIELD, name)
            
        with step(f"Enter surname: {surname}"):
            self.enter_text(OrderPersonInfoPageLocators.SURNAME_FIELD, surname)
        
        with step(f"Enter address: {address}"):
            self.enter_text(OrderPersonInfoPageLocators.ADDRESS_FIELD, address)

        with step(f"Enter station: {station}"):
            self.click_nativ_element(OrderPersonInfoPageLocators.STATION_FIELD)
            station_locator = (By.XPATH, f"//div[@class='Order_Text__2broi' and text()='{station}']")
            self.click_nativ_element(station_locator)

        with step(f"Enter phone: {phone}"):
            self.enter_text(OrderPersonInfoPageLocators.PHONE_FIELD, phone)
            
    @step("Click NEXT_BUTTON")
    def next_button_click(self):
        self.click_element(OrderPersonInfoPageLocators.NEXT_BUTTON)
   



