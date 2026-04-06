from selenium.webdriver.common.by import By

class OrderRentInfoPageLocators: 

    DATE_FIELD = By.XPATH, ".//input[contains(@placeholder, 'Когда')]"
    PERIOD_FIELD = By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']"
    COMMENT_FIELD = By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]"

    LAST_ORDER_BUTTON = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"