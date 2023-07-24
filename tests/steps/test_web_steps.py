import time
from pytest_bdd import scenario, given, when, then, parsers
from tests import drivers, methods


@scenario('../features/webfeatures.feature', "Login with RO valid credentials")
def test_web():
    pass


@given(parsers.parse('User is on the "{web_name}" home page'))
def browser_navigation(web_name):
    drivers.url_browse('details', web_name)


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
#
#
@then(parsers.parse('User should be successfully logged in with "{test}" located on "{testfile}"'))
def verification_login(test, testfile):
    time.sleep(10)
    data_edit = test.replace(" ", ".")
    testfile_edit = testfile.replace(" ", "")
    user_data = drivers.get_data("C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/Identifiers/{}.properties".format(testfile_edit), 'details', data_edit)
    user_path = methods.extract_variable(user_data, testfile_edit)
    user_update = user_path.replace('"', '').replace("\n", "")
    username = drivers.find_ele_xp(user_update).text
    check = drivers.get_data("C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/testData/{}.properties".format(testfile_edit), 'details', data_edit)
    methods.compare(check, username)
    time.sleep(5)


@when(parsers.parse('User enter "{data}" in "{text_box}" on "{testfile}"'))
def enter_credentials(data, text_box, testfile):
    # Create 1 Folder under test as testData
    # data_edit variable should be under testdata folder file name as testfile
    # Create 1 Folder under test as Identifiers
    # data_edit variable should be under identifiers folder file name as testfile
    # Create 1 Folder under test as enm
    # Create same file name for enum -- > identifers variable value
    data_edit = data.replace(" ", ".")
    text_box_edit = text_box.replace(" ", ".")
    testfile_edit = testfile.replace(" ", "")
    print(testfile_edit)
    user_data = drivers.get_data("C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/testData/{}.properties".format(testfile_edit), 'details', data_edit)
    box = drivers.get_data("C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/Identifiers/{}.properties".format(testfile_edit), 'details', text_box_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = box_path.replace('"', '').replace("\n", "")
    box_update_path = drivers.find_ele_xp(box_update)
    methods.clicker(box_update_path)
    methods.writer(user_data)


@then(parsers.parse('User Click on "{button_name}" on "{testfile}"'))
def logging_in(button_name, testfile):
    button_name_edit = button_name.replace(" ", ".")
    testfile_edit = testfile.replace(" ", "")
    box = drivers.get_data("C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/Identifiers/{}.properties".format(testfile_edit), 'details', button_name_edit)
    box_path = methods.extract_variable(box, testfile_edit)
    box_update = box_path.replace('"', '').replace("\n", "")
    box_update_path = drivers.find_ele_xp(box_update)
    methods.clicker(box_update_path)
    time.sleep(5)

