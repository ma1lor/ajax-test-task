import pytest
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.appiumby import By
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)



@pytest.mark.parametrize("email, password", [("test@gmail.com", "password123")])
def test_login_incorrect(driver, email, password):
    time.sleep(3)
    element_locator = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@text="Log In"]'))
    )

    element = driver.find_element(By.XPATH, f'//*[@text="Log In"]')
    element.click()

    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]').send_keys(f'{email}')
    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]').send_keys(f'{password}')

    element_locator = (By.XPATH, f'//*[@text="Log In"]')

    element = driver.find_element(*element_locator)
    element.click()


    element_locator = (By.XPATH, f'//*[@text="Log In"]')

    element = driver.find_element(*element_locator)
         
    assert element.is_displayed()

    driver.back()




@pytest.mark.parametrize("email, password", [("qa.ajax.app.automation@gmail.com", "qa_automation_password")])
def test_login_correct(driver, email, password):
    element_locator = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@text="Log In"]'))
    )

    element = driver.find_element(By.XPATH, f'//*[@text="Log In"]')
    element.click()

    email_locator = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'))
    )

    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]').send_keys(f'{email}')
    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]').send_keys(f'{password}')



    element = driver.find_element(By.XPATH, f'//*[@text="Log In"]')

    element.click()

    
    time.sleep(5)

    text = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.ajaxsystems:id/addFirstHub"]')
    
    assert text.text == 'Add your first hub to start managing the security system'




    
