import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")

def login(driver):
    email = "qa.ajax.app.automation@gmail.com"
    password = "qa_automation_password"

    element_locator = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@text="Log In"]'))
    )

    element = driver.find_element(By.XPATH, f'//*[@text="Log In"]')
    element.click()

    email_locator = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]'))
    )

    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[1]').send_keys(email)
    driver.find_element(By.XPATH, '(//android.widget.EditText[@resource-id="defaultAutomationId"])[2]').send_keys(password)

    element = driver.find_element(By.XPATH, f'//*[@text="Log In"]')
    element.click()

    

    time.sleep(3)  
    
    