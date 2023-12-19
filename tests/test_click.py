import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.appiumby import By
from selenium.common.exceptions import NoSuchElementException
import time
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

@pytest.mark.third
@pytest.mark.parametrize("text", ["Log In", "Create Account"])
def test_clicks(driver, text):
    element_locator = (AppiumBy.XPATH, f'//*[@text="{text}"]')

    element = driver.find_element(*element_locator)

    element.click()

  
    
    driver.back()

