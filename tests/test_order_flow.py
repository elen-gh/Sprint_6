from pages.main_page import MainPage
from pages.order_person_info_page import OrderPersonInfoPage
from pages.order_rent_info_page import OrderRentInfoPage
from pages.order_confirmation_page import OrderConfirmationPage
from pages.order_success_page import OrderSuccessPage
from pages.order_status_page import OrderStatusPage
from src.data import OrderData
import pytest
import allure
import time

class TestOrderFlow:

    @allure. title("Order positive")
    @pytest.mark.parametrize("method_name, user_data", [
        ("order_header_button_click", OrderData.DATA_1),
        ("order_middle_button_click", OrderData.DATA_2),
    ])
    def test_order_flow(self, driver, method_name, user_data):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        getattr(main_page, method_name)()

        order_person_info_page = OrderPersonInfoPage(driver)
        order_person_info_page.fill_order_person_info(**user_data)
        order_person_info_page.next_button_click()

        order_rent_info_page = OrderRentInfoPage(driver)
        order_rent_info_page.fill_order_rent_info(**user_data)
        order_rent_info_page.last_order_button_click()
    
        order_confirmation_page = OrderConfirmationPage(driver)
        order_confirmation_page.order_yes_button_click()

        order_success_page = OrderSuccessPage(driver)
        assert order_success_page.order_status_button_visible()

        time.sleep(1)
        order_success_page.order_status_button_click()
        order_status_page = OrderStatusPage(driver)
        order_status_page.click_scooter_logo()
        assert main_page.order_middle_button_visible()

        main_page.click_yandex_logo()
        current_url = main_page.wait_for_new_window_and_check_url("dzen.ru")
        assert "dzen.ru" in current_url
        

        


       

    