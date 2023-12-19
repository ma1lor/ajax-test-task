import pytest
from appium.webdriver.common.appiumby import AppiumBy
import time

@pytest.mark.second
@pytest.mark.parametrize("text", ["Log In", "Create Account"])
def test_clicks(driver, text):
    element_locator = (AppiumBy.XPATH, f'//*[@text="{text}"]')

    element = driver.find_element(*element_locator)
    assert element.is_displayed() == True

    assert element.is_enabled() == True

    element.click()
    driver.back()
    time.sleep(4)
