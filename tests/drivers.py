import os
from tests import methods
from tests.UtilityFactory import waitUtilities

# import subprocess

# subprocess.Popen("appium", shell=True)

# finding the path to root directory
current_script_path = os.path.abspath(__file__)
root_dir = os.path.dirname(current_script_path)
# formulating dynamic paths
android_path = root_dir + '/Android/Capabilities.json'
config_path = root_dir + '/config.properties'
# getting data or values from config file that are essential for driver setup
platform_source = methods.get_data(config_path, "platform", "source")
appium_driver_url = methods.get_data(config_path, "platform", "appium_driver_url")

appium_apk_name = methods.get_data(config_path, "platform", "apk_name")
appium_device_name = methods.get_data(config_path, "platform", "android_device_name")
appium_platform_name = methods.get_data(config_path, "platform", "platform_name")
appium_platform_version = methods.get_data(config_path, "platform", "platform_version")

# formulating dynamic paths
apk_path = root_dir + '/APK/' + appium_apk_name
json_file_path = root_dir + '/Android/Capabilities.json'


# initiating drivers based on the source condition in the config file
# do verify the source in the config file for the correct driver to be initiated
if platform_source == "web":
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    selenium_driver = methods.get_data(config_path, "platform", "selenium_driver")
    match selenium_driver:
        case "Edge":
            driver = webdriver.Edge()
            driver.set_page_load_timeout(40)
            driver.maximize_window()
        case "Chrome":
            driver = webdriver.Chrome()
            driver.set_page_load_timeout(40)
            driver.maximize_window()
elif platform_source == "mobile":
    from appium import webdriver
    from appium.webdriver.common.appiumby import AppiumBy as By
    # dynamically adding the values to the Capabilities for initiating the driver with the correct Capabilities
    methods.json_data_assigning("appium:app", apk_path, json_file_path)
    methods.json_data_assigning("appium:deviceName", appium_device_name, json_file_path)
    methods.json_data_assigning("appium:platformVersion", appium_platform_version, json_file_path)
    methods.json_data_assigning("platformName", appium_platform_name, json_file_path)
    desired_cap = methods.json_data_get(android_path)
    driver = webdriver.Remote(appium_driver_url, desired_cap, proxy=None)
    # removing the values from the Capabilities after the driver is once initiated
    methods.json_data_removal("appium:app", json_file_path)
    methods.json_data_removal("appium:deviceName", json_file_path)
    methods.json_data_removal("appium:platformVersion", json_file_path)
    methods.json_data_removal("platformName", json_file_path)


def find_ele_xp(xpath):
    waitUtilities.elementToBe_Visible(driver, xpath)
    element = driver.find_element(By.XPATH, xpath)
    return element


def clicker(variable):
    element = waitUtilities.elementToBe_Clickable(driver, variable)
    element.click()


def switch_to_child_window():
    child = driver.window_handles[1]
    driver.switch_to.window(child)


def switch_to_parent_window():
    parent = driver.window_handles[0]
    driver.switch_to.window(parent)


def select_dropdown(data, xpath):
    select = Select(waitUtilities.elementToBe_Clickable(driver, xpath))
    select.select_by_visible_text(data)


def scroll_to_element(element):
    while not element.location_once_scrolled_into_view:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start', behavior: 'instant'});", element)


def switch_driver():
    global driver
    driver.quit()
    platform = methods.get_data(config_path, "platform", "source")
    if platform == "mobile":
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import Select
        selenium_driver = methods.get_data(config_path, "platform", "selenium_driver")
        match selenium_driver:
            case "Edge":
                driver = webdriver.Edge()
                driver.set_page_load_timeout(40)
                driver.maximize_window()
            case "Chrome":
                driver = webdriver.Chrome()
                driver.set_page_load_timeout(40)
                driver.maximize_window()
        methods.properties_file_updater(config_path, 'platform', 'source', 'web')
    elif platform == "web":
        from appium import webdriver
        from appium.webdriver.common.appiumby import AppiumBy as By
        # dynamically adding the values to the Capabilities for initiating the driver with the correct Capabilities
        methods.json_data_assigning("appium:app", apk_path, json_file_path)
        methods.json_data_assigning("appium:deviceName", appium_device_name, json_file_path)
        methods.json_data_assigning("appium:platformVersion", appium_platform_version, json_file_path)
        methods.json_data_assigning("platformName", appium_platform_name, json_file_path)
        desired_cap = methods.json_data_get(android_path)
        driver = webdriver.Remote(appium_driver_url, desired_cap, proxy=None)
        # removing the values from the Capabilities after the driver is once initiated
        methods.json_data_removal("appium:app", json_file_path)
        methods.json_data_removal("appium:deviceName", json_file_path)
        methods.json_data_removal("appium:platformVersion", json_file_path)
        methods.json_data_removal("platformName", json_file_path)
        methods.properties_file_updater(config_path, 'platform', 'source', 'mobile')
