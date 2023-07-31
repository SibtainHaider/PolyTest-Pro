from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.maximize_window()


def find_ele_xp(var):
    return driver.find_element(By.XPATH, var)


def switch_to_child():
    child = driver.window_handles[1]
    # switch to browser tab
    driver.switch_to.window(child)


def select_dropdown(data, xpath):
    # select = Select(driver.find_element(By.ID, element_id))
    # select.select_by_visible_text(data)
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))))
    select.select_by_visible_text(data)
