import time
from tests import methods
import os

current_script_path = os.path.abspath(__file__)
root_dir = os.path.dirname(current_script_path)

android_path = root_dir + '/Android/Capabilities.json'
config_path = root_dir + "/Identifiers/config.properties"

platform_name = methods.get_data(config_path, "platform", "source")
appium_driver_url = methods.get_data(config_path, "platform", "appium_driver_url")
if platform_name == "web":
    import selenium
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Edge()
    driver.maximize_window()
    methods.properties_file_updater(config_path, 'platform', 'source', 'mobile')
elif platform_name == "mobile":
    import appium
    from appium import webdriver
    from appium.webdriver.common.appiumby import AppiumBy as By
    desired_cap = methods.json_data(android_path)
    driver = webdriver.Remote(appium_driver_url, desired_cap, proxy=None)
    methods.properties_file_updater(config_path, 'platform', 'source', 'web')


def find_ele_xp(var):
    element = driver.find_element(By.XPATH, var)
    return element


def switch_to_child_window():
    child = driver.window_handles[1]
    driver.switch_to.window(child)


def switch_to_parent_window():
    parent = driver.window_handles[0]
    driver.switch_to.window(parent)


def select_dropdown(data, xpath):
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))))
    select.select_by_visible_text(data)


def scroll_to_element(element):
    while not element.location_once_scrolled_into_view:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start', behavior: 'instant'});", element)
        time.sleep(0.5)


def delete_driver():
    global driver
    driver.quit()
    platform = methods.get_data(config_path, "platform", "source")
    if platform == "web":
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import Select
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        driver = webdriver.Edge()
        driver.maximize_window()
        methods.properties_file_updater(config_path, 'platform', 'source', 'mobile')
    elif platform == "mobile":
        from appium import webdriver
        from appium.webdriver.common.appiumby import AppiumBy as By
        driver = webdriver.Remote(appium_driver_url, desired_cap, proxy=None)
        methods.properties_file_updater(config_path, 'platform', 'source', 'web')
