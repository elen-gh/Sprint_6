from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from allure import step

class OrderStatusPage(BasePage):

    @step("Click LOGO_SCOOTER_BUTTON")
    def click_scooter_logo(self):
        self.click_element(BasePageLocators.LOGO_SCOOTER_BUTTON)

