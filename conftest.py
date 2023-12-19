import pytest
import subprocess
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.options.android import UiAutomator2Options
import time
from get_udid import get_device_udid



capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName=get_device_udid(),
    appPackage='com.ajaxsystems',
    appActivity='com.ajaxsystems.ui.activity.LauncherActivity',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723/wd/hub'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)



@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)
    


@pytest.fixture(scope='session')
def driver(request):
    driver_instance = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)


    yield driver_instance