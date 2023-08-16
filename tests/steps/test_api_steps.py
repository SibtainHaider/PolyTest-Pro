from pytest_bdd import scenario, given, when, then, parsers
from tests import methods
import requests
import os

current_script_path = os.path.abspath(__file__)
path1 = os.path.dirname(os.path.dirname(current_script_path))


@scenario('../features/api_testing.feature', 'Testing the API')
def test_api():
    pass


check = path1 + '/testData/API_Data/check.properties'
get = path1 + '/testData/API_Data/get.properties'
post = path1 + '/testData/API_Data/post.properties'
put = path1 + '/testData/API_Data/put.properties'
delete = path1 + '/testData/API_Data/delete.properties'
api_path = path1 + '/API_Requests/'


@given(parsers.parse('There is an API with "{link}"'))
def API_Check(link):
    link_edit = methods.data_mod(link)
    url = methods.get_data(check, 'details', link_edit)
    resp = requests.get(url, verify=False)
    assert (resp.status_code == 200), "The error code is: " + str(resp.status_code)


@then(parsers.parse('User Hit Get "{link}"'))
def API_get(link):
    link_edit = methods.data_mod(link)
    url = methods.get_data(get, 'details', link_edit)
    resp = requests.get(str(url), verify=False)
    assert (resp.status_code == 200), "The error code is: " + str(resp.status_code)


@then(parsers.parse('User Hit Post "{link}" with "{post_json}"'))
def API_post(link, post_json):
    json_edit = methods.file_mod(post_json)
    api_path_updated = api_path + json_edit + '.json'
    data = methods.json_data_get(api_path_updated)
    link_edit = methods.data_mod(link)
    url = methods.get_data(post, 'details', link_edit)
    resp = requests.post(url, data=data, verify=False)
    Data = resp.json()
    assert (resp.status_code == 201), "The error code is: " + str(resp.status_code)
    assert (Data.get('name') == data.get('name')), "User created with wrong data: " + str(Data.get('name'))


@then(parsers.parse('User Hit Put "{link}" with "{post_json}"'))
def API_update(link, post_json):
    json_edit = methods.file_mod(post_json)
    api_path_updated = api_path + json_edit + '.json'
    data = methods.json_data_get(api_path_updated)
    link_edit = methods.data_mod(link)
    url = methods.get_data(put, 'details', link_edit)
    resp = requests.put(url, data=data, verify=False)
    Data = resp.json()
    assert (resp.status_code == 200), "The error code is: " + str(resp.status_code)
    assert (Data.get('name') == data.get('name')), "User created with wrong data: " + str(Data.get('name'))


@then(parsers.parse('User Hit Delete "{link}"'))
def API_delete(link):
    link_edit = methods.data_mod(link)
    url = methods.get_data(delete, 'details', link_edit)
    resp = requests.delete(str(url), verify=False)
    assert (resp.status_code == 204), "The error code is: " + str(resp.status_code)
