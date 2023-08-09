from pytest_bdd import scenario, given, when, then, parsers
from tests import methods
import requests


@scenario('../features/api_testing.feature', 'Testing the API')
def test_api():
    pass


check = 'C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/API_Data/check.properties'
get = 'C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/API_Data/get.properties'
post = 'C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/API_Data/post.properties'
put = 'C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/API_Data/put.properties'
delete = 'C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/API_Data/delete.properties'
api_path = 'C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/Requests/'


@given(parsers.parse('There is an API with "{link}"'))
def API_Check(link):
    link_edit = methods.data_mod(link)
    url = methods.get_data(check, 'details', link_edit)
    resp = requests.get(url, verify=False)
    print(resp.status_code)
    assert (resp.status_code == 200), "The error code is: " + str(resp.status_code)


@then(parsers.parse('User Hit Get "{link}"'))
def API_get(link):
    link_edit = methods.data_mod(link)
    url = methods.get_data(get, 'details', link_edit)
    resp = requests.get(str(url), verify=False)
    print(resp.status_code)
    assert (resp.status_code == 200), "The error code is: " + str(resp.status_code)


@then(parsers.parse('User Hit Post "{link}" with "{post_json}"'))
def API_post(link, post_json):
    json_edit = methods.file_mod(post_json)
    data = methods.json_data(api_path, json_edit)
    link_edit = methods.data_mod(link)
    url = methods.get_data(post, 'details', link_edit)
    resp = requests.post(url, data=data, verify=False)
    print(resp.status_code)
    dataa = resp.json()
    assert (resp.status_code == 201), "The error code is: " + str(resp.status_code)
    assert (dataa.get('name') == data.get('name')), "User created with wrong data: " + str(dataa.get('name'))


@then(parsers.parse('User Hit Put "{link}" with "{post_json}"'))
def API_update(link, post_json):
    json_edit = methods.file_mod(post_json)
    data = methods.json_data(api_path, json_edit)
    link_edit = methods.data_mod(link)
    url = methods.get_data(put, 'details', link_edit)
    resp = requests.put(url, data=data, verify=False)
    print(resp.status_code)
    dataa = resp.json()
    assert (resp.status_code == 200), "The error code is: " + str(resp.status_code)
    assert (dataa.get('name') == data.get('name')), "User created with wrong data: " + str(dataa.get('name'))


@then(parsers.parse('User Hit Delete "{link}"'))
def API_delete(link):
    link_edit = methods.data_mod(link)
    url = methods.get_data(delete, 'details', link_edit)
    resp = requests.delete(str(url), verify=False)
    print(resp.status_code)
    assert (resp.status_code == 204), "The error code is: " + str(resp.status_code)
