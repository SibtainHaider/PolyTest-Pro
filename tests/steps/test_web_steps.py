import time
from pytest_bdd import scenario, given, when, then, parsers
from tests import drivers, methods


@scenario('../features/webfeatures.feature', "Login with RO valid credentials")
def test_web():
    pass


@given(parsers.parse('I am on the "{web_name}" home page'))
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
@then(parsers.parse('I should be successfully logged in with "{test}"'))
def verification_login(test):
    time.sleep(10)
    verification = drivers.find_ele_xp('details', 'login_verification_text').text
    check = drivers.get_cred('details', test)
    methods.compare(check, verification)
    time.sleep(5)


@when(parsers.parse('User enter "{data}" in "{text_box}" on "{testfile}"'))
def enter_credentials(data, text_box, testfile):
    data_edit = data.replace(" ", ".")
    text_box_edit = text_box.replace(" ", "_")
    testfile_edit = testfile.replace(" ", "")
    element = drivers.get_cred('details', data_edit)
    box = methods.extract_variable(text_box_edit, testfile_edit)
    box_update = box.replace("'", "").replace("\n", "")
    box_path = drivers.find_ele_xp('details', box_update)
    methods.clicker(box_path)
    methods.writer(element)


@then(parsers.parse('User Click on "{button_name}" on "{testfile}"'))
def logging_in(button_name, testfile):
    button_name_edit = button_name.replace(" ", "_")
    testfile_edit = testfile.replace(" ", "")
    box = methods.extract_variable(button_name_edit, testfile_edit)
    box_update = box.replace("'", "").replace("\n", "")
    box_path = drivers.find_ele_xp('details', box_update)
    methods.clicker(box_path)
    time.sleep(5)
