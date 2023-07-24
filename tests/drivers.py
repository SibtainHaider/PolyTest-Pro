from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser

config1 = configparser.RawConfigParser()
config1.read('test.properties')

driver = webdriver.Edge()


def get_data(file_name, heading, variable):
    config = configparser.RawConfigParser()
    config.read(file_name)
    return config.get(heading, variable)

#
# def url_browse(details, url):
#     driver.get(config1.get(details, url))


def find_ele_xp(var):
    return driver.find_element(By.XPATH, var)


# def get_cred(heading, var):
#     return config.get(heading, var)

