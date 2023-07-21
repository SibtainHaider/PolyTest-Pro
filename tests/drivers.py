from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser

config = configparser.RawConfigParser()
config.read('test.properties')

driver = webdriver.Edge()


def url_browse(details, url):
    driver.get(config.get(details, url))


def find_ele_xp(details, var):
    return driver.find_element(By.XPATH, config.get(details, var))


def get_cred(heading, var):
    return config.get(heading, var)
