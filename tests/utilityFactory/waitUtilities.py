import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests import methods

current_script_path = os.path.abspath(__file__)
path1 = os.path.dirname(os.path.dirname(current_script_path))
config_path = path1 + '/config.properties'

platform_source = methods.get_data(config_path, "platform", "source")

if platform_source == "web":
    from selenium.webdriver.common.by import By
elif platform_source == "mobile":
    from appium.webdriver.common.appiumby import AppiumBy as By


POLL_FREQUENCY = 0.1
TIMEOUT = 10


def elementToBe_Visible(driver, Xpath):
    WebDriverWait(driver, TIMEOUT, POLL_FREQUENCY).until(EC.visibility_of_element_located((By.XPATH, Xpath)))


def elementToBe_Clickable(driver, element):
    return WebDriverWait(driver, TIMEOUT, POLL_FREQUENCY).until(EC.element_to_be_clickable(element))


# def wait_for_page_to_load(driver):
#     wait = WebDriverWait(driver, TIMEOUT)
#     wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
