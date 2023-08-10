import time


from tests import methods

android_path = 'C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/Android/'
config_path = "C:\\Users\\msibtain.haider\\Desktop\\Python_Automation1\\tests\\Identifiers\\config.properties"

platform_name = methods.get_data(config_path, "platform", "source")
if platform_name == "web":
    from selenium import webdriver
    # from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Edge()
    driver.maximize_window()
    methods.properties_updater(config_path, 'platform', 'source', 'mobile')
elif platform_name == "mobile":
    from appium import webdriver
    from appium.webdriver.common.appiumby import AppiumBy as By
    desired_cap = methods.json_data(android_path, 'Capabilities')
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap, proxy=None)
    # methods.properties_updater(config_path, 'platform', 'source', 'web')


def find_ele_xp(var):
    element = driver.find_element(By.XPATH, var)
    return element


def switch_to_child():
    child = driver.window_handles[1]
    driver.switch_to.window(child)


def select_dropdown(data, xpath):
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))))
    select.select_by_visible_text(data)


def element_focus(element):
    while not element.location_once_scrolled_into_view:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start', behavior: 'instant'});", element)
        time.sleep(0.5)
