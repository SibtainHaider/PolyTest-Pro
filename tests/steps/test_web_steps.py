import time
from pytest_bdd import scenario, given, when, then, parsers
from tests import drivers, methods, zipper
import allure


@scenario('../features/webfeatures.feature', "Login with RO valid credentials")
def test_web():
    pass


@scenario('../features/ess_dashboard.feature', "User dashboard")
def test_ess_dashboard():
    pass


path1 = "C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/"


@allure.severity(allure.severity_level.NORMAL)
@given(parsers.parse('User is on the "{web_name}" page on "{testfile}"'))
def browser_navigation(web_name, testfile):
    web_name_edit = methods.data_mod(web_name)
    testfile_edit = methods.file_mod(testfile)
    path2 = "testData/{}.properties".format(testfile_edit)
    url = drivers.get_data(path1 + path2, 'details', web_name_edit)
    drivers.driver.get(url)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User is verified with "{test}" located on "{testfile}"'))
def verification_login(test, testfile):
    time.sleep(10)
    data_edit = methods.data_mod(test)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    user_data = drivers.get_data(path1 + path2, 'details', data_edit)
    user_path = methods.extract_variable(user_data, testfile_edit)
    user_update = methods.extraction_mod(user_path)
    username = drivers.find_ele_xp(user_update).text
    path3 = "testData/{}.properties".format(testfile_edit)
    check = drivers.get_data(path1 + path3, 'details', data_edit)
    methods.compare(check, username)
    time.sleep(5)


@allure.severity(allure.severity_level.NORMAL)
@when(parsers.parse('User enter "{data}" in "{text_box}" on "{testfile}"'))
def enter_credentials(data, text_box, testfile):
    data_edit = methods.data_mod(data)
    text_box_edit = methods.data_mod(text_box)
    testfile_edit = methods.file_mod(testfile)
    print(testfile_edit)
    path3 = "testData/{}.properties".format(testfile_edit)
    user_data = drivers.get_data(path1 + path3, 'details', data_edit)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = drivers.get_data(path1 + path2, 'details', text_box_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    box_update_path = drivers.find_ele_xp(box_update)
    methods.clicker(box_update_path)
    methods.writer(user_data)


@allure.severity(allure.severity_level.NORMAL)
@then(parsers.parse('User Click on "{button_name}" on "{testfile}"'))
def logging_in(button_name, testfile):
    button_name_edit = methods.data_mod(button_name)
    testfile_edit = methods.file_mod(testfile)
    path2 = "/Identifiers/{}.properties".format(testfile_edit)
    box = drivers.get_data(path1 + path2, 'details', button_name_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = methods.extraction_mod(box_path)
    box_update_path = drivers.find_ele_xp(box_update)
    methods.clicker(box_update_path)
    time.sleep(5)


# @when(parsers.parse('I enter "{user}" in "{box}"'))
# def enter_credentials(user, box):
#     # variable replace space with .
#     element = drivers.find_ele_xp('details', box)
#     methods.clicker(element)
#     configure = drivers.get_cred('details', user)
#     methods.writer(configure)
#
#
# @then(parsers.parse('I click on the "{text}" button'))
# def logging_in(text):
#     element = drivers.find_ele_xp('details', text)
#     methods.clicker(element)
#
#
# @then(parsers.parse('Search for "{variable_name}" in "{file_name}"'))
# def get_var_fromfile(variable_name, file_name):
#     output = methods.extract_variable(variable_name, file_name)
#     print(output)
