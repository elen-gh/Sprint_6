from pages.main_page import MainPage
from src.data import FaqInfo
import pytest
import allure

class TestFAQList:
    @allure. title("FAQ list")
    @pytest.mark.parametrize("click_method, visibility_method, expected_text", [
        ("faq_button_0_click", "faq_info_0_visible", FaqInfo.faq_info_0),
        ("faq_button_1_click", "faq_info_1_visible", FaqInfo.faq_info_1),
        ("faq_button_2_click", "faq_info_2_visible", FaqInfo.faq_info_2),
        ("faq_button_3_click", "faq_info_3_visible", FaqInfo.faq_info_3),
        ("faq_button_4_click", "faq_info_4_visible", FaqInfo.faq_info_4),
        ("faq_button_5_click", "faq_info_5_visible", FaqInfo.faq_info_5),
        ("faq_button_6_click", "faq_info_6_visible", FaqInfo.faq_info_6),
        ("faq_button_7_click", "faq_info_7_visible", FaqInfo.faq_info_7),
    ])
    
    def test_faq_list(self, driver, click_method, visibility_method, expected_text):
        main_page = MainPage(driver)
        getattr(main_page, click_method)()
        element = getattr(main_page, visibility_method)()
        assert element.text == expected_text

    