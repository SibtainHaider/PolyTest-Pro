from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()


def find_ele_xp(var):
    return driver.find_element(By.XPATH, var)
