from selenium.webdriver.common.by import By

class OrderPersonInfoPageLocators:

    NAME_FIELD = By.XPATH, ".//input[@placeholder='* Имя']"
    SURNAME_FIELD = By.XPATH, ".//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, ".//input[contains(@placeholder, 'Адрес')]"
    STATION_FIELD = By.XPATH, ".//input[@placeholder='* Станция метро']"
    PHONE_FIELD = By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"

    NEXT_BUTTON = By.XPATH, "//button[text()='Далее']"