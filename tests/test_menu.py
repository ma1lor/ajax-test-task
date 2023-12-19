import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.mark.usefixtures("login")
@pytest.mark.parametrize('menu_item', [
    ('//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]'),
    ('(//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"])'),
    ('(//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"])'),
    ('(//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Video Surveillance"])')
])

def test_app_settings(driver, menu_item):
    menu = driver.find_element(By.XPATH, '(//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"])')
    menu.click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, menu_item))
    )

    app_settings = driver.find_element(By.XPATH, menu_item)
    app_settings.click()

    driver.back()





    

