import time
from pytest_bdd import scenario, given, when, then, parsers
from tests import drivers, methods
import allure


@scenario('../features/sapphire_checkout.feature', "Checking the purchase feature")
def test_sapphire():
    pass


# @scenario('../features/j._checkout.feature', "Checking the purchase feature")
# def test_JJ():
#     pass


# @scenario('../features/webfeatures.feature', "Login with RO valid credentials")
# def test_web():
#     pass
#
#
# @scenario('../features/ess_dashboard.feature', "User dashboard")
# def test_ess_dashboard():
#     pass


# @scenario('../features/khaadi_checkout.feature', "Checking the purchase feature")
# def test_khaadi():
#     pass


path1 = "C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/"


@allure.severity(allure.severity_level.NORMAL)
@given(parsers.parse('User is on the "{web_name}" page on "{testfile}"'))
def browser_navigation(web_name, testfile):
    web_name_edit = methods.data_mod(web_name)
    testfile_edit = methods.file_mod(testfile)
    path2 = "testData/{}.properties".format(testfile_edit)
    url = methods.get_data(path1 + path2, 'details', web_name_edit)
    drivers.driver.get(url)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User is verified with "{test}" located on "{testfile}"'))
def verification_login(test, testfile):
    time.sleep(10)
    data_edit = methods.data_mod(test)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    user_data = methods.get_data(path1 + path2, 'details', data_edit)
    user_path = methods.extract_variable(user_data, testfile_edit)
    user_update = methods.extraction_mod(user_path)
    username = drivers.find_ele_xp(user_update).text
    path3 = "testData/{}.properties".format(testfile_edit)
    check = methods.get_data(path1 + path3, 'details', data_edit)
    methods.compare(check, username)
    time.sleep(5)


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
    # drivers.element_focus(box_update_path)
    methods.clicker(box_update_path)
    time.sleep(2)


@allure.severity(allure.severity_level.NORMAL)
@then("The browser switches windows")
def switch_tabs():
    drivers.switch_to_child()


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User enter "{data}" in "{text_box}" on "{testfile}"'))
def enter_credentials(data, text_box, testfile):
    data_edit = methods.data_mod(data)
    text_box_edit = methods.data_mod(text_box)
    testfile_edit = methods.file_mod(testfile)
    path3 = "testData/{}.properties".format(testfile_edit)
    user_data = methods.get_data(path1 + path3, 'details', data_edit)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = methods.get_data(path1 + path2, 'details', text_box_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    box_update_path = drivers.find_ele_xp(box_update)
    methods.clicker(box_update_path)
    methods.writer(user_data)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User selects "{data}" on "{dropdown}" from "{testfile}"'))
def select_dropdown(data, dropdown, testfile):
    data_edit = methods.data_mod(data)
    dropdown_edit = methods.data_mod(dropdown)
    testfile_edit = methods.file_mod(testfile)
    path3 = "testData/{}.properties".format(testfile_edit)
    user_data = methods.get_data(path1 + path3, 'details', data_edit)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = methods.get_data(path1 + path2, 'details', dropdown_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    drivers.select_dropdown(user_data, box_update)


@then(parsers.parse('User scrolls to "{element}" on "{testfile}"'))
def scroll_to_element(element, testfile):
    element_edit = methods.data_mod(element)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = methods.get_data(path1 + path2, 'details', element_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    box_update_path = drivers.find_ele_xp(box_update)
    drivers.element_focus(box_update_path)
