from allure_commons.types import AttachmentType
from pytest_bdd import given, when, then, parsers
from tests import drivers, methods
import allure
from appium.webdriver.common.touch_action import TouchAction
import os

current_script_path = os.path.abspath(__file__)
path1 = os.path.dirname(os.path.dirname(current_script_path))


@allure.severity(allure.severity_level.NORMAL)
@given(parsers.parse('User is on the "{web_name}" page on "{testfile}"'))
def browser_navigation(web_name, testfile):
    web_name_edit = methods.data_mod(web_name)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/testData/{}.properties".format(testfile_edit)
    url = methods.get_data(path1 + path2, 'details', web_name_edit)
    drivers.driver.get(url)
    allure.attach(drivers.driver.get_screenshot_as_png(), name="url_browse", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User is verified with "{test}" located on "{testfile}"'))
def verification_login(test, testfile):
    data_edit = methods.data_mod(test)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    user_data = methods.get_data(path1 + path2, 'details', data_edit)
    user_path = methods.extract_variable(user_data, testfile_edit)
    user_update = methods.extraction_mod(user_path)
    username = drivers.find_ele_xp(user_update).text
    path3 = "/testData/{}.properties".format(testfile_edit)
    check = methods.get_data(path1 + path3, 'details', data_edit)
    methods.compare(check, username)
    allure.attach(drivers.driver.get_screenshot_as_png(), name="verification", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User Click on "{button_name}" on "{testfile}"'))
def click(button_name, testfile):
    button_name_edit = methods.data_mod(button_name)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = methods.get_data(path1 + path2, 'details', button_name_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    box_update_path = drivers.find_ele_xp(box_update)
    drivers.clicker(box_update_path)
    allure.attach(drivers.driver.get_screenshot_as_png(), name="click", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then("The browser switches window to child")
def switch_tab_to_child():
    drivers.switch_to_child_window()
    allure.attach(drivers.driver.get_screenshot_as_png(), name="switch_tab_to_child", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then("The browser switches window to parent")
def switch_tab_to_parent():
    drivers.switch_to_parent_window()
    allure.attach(drivers.driver.get_screenshot_as_png(), name="switch_tab_to_parent", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User enter "{data}" in "{text_box}" on "{testfile}"'))
def enter_credentials(data, text_box, testfile):
    data_edit = methods.data_mod(data)
    text_box_edit = methods.data_mod(text_box)
    testfile_edit = methods.file_mod(testfile)
    path3 = "/testData/{}.properties".format(testfile_edit)
    user_data = methods.get_data(path1 + path3, 'details', data_edit)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = methods.get_data(path1 + path2, 'details', text_box_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    box_update_path = drivers.find_ele_xp(box_update)
    drivers.clicker(box_update_path)
    methods.writer(user_data)
    allure.attach(drivers.driver.get_screenshot_as_png(), name="enter_credentials", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User selects "{data}" on "{dropdown}" from "{testfile}"'))
def select_dropdown(data, dropdown, testfile):
    data_edit = methods.data_mod(data)
    dropdown_edit = methods.data_mod(dropdown)
    testfile_edit = methods.file_mod(testfile)
    path3 = "/testData/{}.properties".format(testfile_edit)
    user_data = methods.get_data(path1 + path3, 'details', data_edit)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = methods.get_data(path1 + path2, 'details', dropdown_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    drivers.select_dropdown(user_data, box_update)
    allure.attach(drivers.driver.get_screenshot_as_png(), name="dropdown", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User scrolls to "{element}" on "{testfile}"'))
def scroll_to_web_element(element, testfile):
    element_edit = methods.data_mod(element)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = methods.get_data(path1 + path2, 'details', element_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    box_update_path = drivers.find_ele_xp(box_update)
    drivers.scroll_to_element(box_update_path)
    allure.attach(drivers.driver.get_screenshot_as_png(), name="scroll", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User scrolls with "{x1}", "{y1}" to "{x2}", "{y2}" "{number}" times'))
def scroll_to_app_element(x1, y1, x2, y2, number, path):
    x1_get = methods.get_data(path, 'details', x1)
    x2_get = methods.get_data(path, 'details', x2)
    y1_get = methods.get_data(path, 'details', y1)
    y2_get = methods.get_data(path, 'details', y2)
    number_get = methods.get_data(path, 'details', number)
    for i in range(number_get):
        touch = TouchAction(drivers.driver)
        touch.press(x1_get, y1_get).move_to(x2_get, y2_get).release().perform()
    allure.attach(drivers.driver.get_screenshot_as_png(), name="scroll", attachment_type=AttachmentType.PNG)


@allure.severity(allure.severity_level.NORMAL)
@then("User switches the driver")
def Switch_driver():
    drivers.switch_driver()
