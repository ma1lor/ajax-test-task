import pytest
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.skip
@pytest.mark.parametrize("email, password", [("test@gmail.com", "password123")])
def test_login_incorrect(driver, email, password):

    element_locator = (By.XPATH, f'//*[@text="Log In"]')

    element = driver.find_element(*element_locator)

    element.click()


    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]').send_keys(f'{email}')
    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]').send_keys(f'{password}')
    
    element_locator = (By.XPATH, f'//*[@text="Log In"]')

    element = driver.find_element(*element_locator)

    element.click()

    time.sleep(5)

    element_locator = (By.XPATH, f'//*[@text="Log In"]')

    element = driver.find_element(*element_locator)
         
    assert element.is_displayed()

    driver.back()




@pytest.mark.parametrize("email, password", [("qa.ajax.app.automation@gmail.com", "qa_automation_password")])
def test_login_correct(driver, email, password):

    element_locator = (By.XPATH, f'//*[@text="Log In"]')

    element = driver.find_element(*element_locator)

    element.click()


    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]').send_keys(f'{email}')
    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]').send_keys(f'{password}')
    
    element_locator = (By.XPATH, f'//*[@text="Log In"]')

    element = driver.find_element(*element_locator)

    element.click()

    time.sleep(5)

    text = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/addFirstHub"]')
    
    assert text.text == 'Add your first hub to start managing the security system'




    
