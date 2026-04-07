from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from allure import step

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @step("Click ORDER_HEADER_BUTTON")
    def order_header_button_click(self):
        self.click_element(MainPageLocators.ORDER_HEADER_BUTTON)

    @step("Click ORDER_MIDDLE_BUTTON")
    def order_middle_button_click(self):
        self.click_element(MainPageLocators.ORDER_MIDDLE_BUTTON)

    def order_middle_button_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.ORDER_MIDDLE_BUTTON)
        return element
    
    @step("Click LOGO_YANDEX_BUTTON")
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.LOGO_YANDEX_BUTTON)

    def wait_for_new_window_and_check_url(self, expected_url_part):
        self.switch_to_last_window()
        self.wait_for_url_contains(expected_url_part)
        return self.get_current_url()

    @step("Click FAQ_BUTTON_0")
    def faq_button_0_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_0)

    def faq_info_0_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_0)
        return element
    
    @step("Click FAQ_BUTTON_1")
    def faq_button_1_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_1)

    def faq_info_1_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_1)
        return element
    
    @step("Click FAQ_BUTTON_2")
    def faq_button_2_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_2)

    def faq_info_2_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_2)
        return element
    
    @step("Click FAQ_BUTTON_3")
    def faq_button_3_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_3)

    def faq_info_3_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_3)
        return element
    
    @step("Click FAQ_BUTTON_4")
    def faq_button_4_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_4)

    def faq_info_4_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_4)
        return element
    
    @step("Click FAQ_BUTTON_5")
    def faq_button_5_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_5)

    def faq_info_5_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_5)
        return element
    
    @step("Click FAQ_BUTTON_6")
    def faq_button_6_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_6)

    def faq_info_6_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_6)
        return element
    
    @step("Click FAQ_BUTTON_7")
    def faq_button_7_click(self):
        self.click_element(MainPageLocators.FAQ_BUTTON_7)

    def faq_info_7_visible(self):
        element = self.wait_for_element_visible(MainPageLocators.FAQ_INFO_7)
        return element