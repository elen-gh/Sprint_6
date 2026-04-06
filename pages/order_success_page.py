from pages.base_page import BasePage
from allure import step
from locators.order_success_page_locators import OrderSuccessPageLocators

class OrderSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @step("Click ORDER_STATUS_BUTTON")
    def order_status_button_click(self):
        self.click_element(OrderSuccessPageLocators.ORDER_STATUS_BUTTON)

    def order_status_button_visible(self):
        element = self.wait_for_element_visible(OrderSuccessPageLocators.ORDER_STATUS_BUTTON)
        return element