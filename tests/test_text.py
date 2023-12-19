import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)



@pytest.mark.first
@pytest.mark.parametrize("text", ["Log In", "Create Account"])
def test_correct_text(driver, text):
    element_locator = (AppiumBy.XPATH, f'//*[@text="{text}"]')

    element = driver.find_element(*element_locator)
    assert element.is_displayed() == True


@pytest.mark.second
@pytest.mark.parametrize("text", ["Login", "Register"])
def test_invalid_text(driver, text):
    element_locator = (AppiumBy.XPATH, f'//*[@text="{text}"]')

    with pytest.raises(NoSuchElementException):
        driver.find_element(*element_locator)



