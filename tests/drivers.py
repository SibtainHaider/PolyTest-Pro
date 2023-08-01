import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.maximize_window()


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
