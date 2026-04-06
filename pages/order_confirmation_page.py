from pages.base_page import BasePage 
from allure import step
from locators.order_confirmation_page_locators import OrderConfirmationPageLocators

class OrderConfirmationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @step("Click ORDER_YES_BUTTON")
    def order_yes_button_click(self):
        self.click_element(OrderConfirmationPageLocators.ORDER_YES_BUTTON)