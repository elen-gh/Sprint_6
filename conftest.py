import pytest
from selenium import webdriver
from src.config import Config

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(Config.BASE_URL)
    yield browser
    browser.quit()

