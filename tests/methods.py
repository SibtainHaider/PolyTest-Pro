import json
import pyautogui as py
import configparser


def clicker(variable):

    variable.click()


def writer(value):
    py.write(value)


def compare(value1, value2):
    if value1 in value2:
        pass
    else:
        exit()


def extract_variable(variable_name, file_name):
    file = open("C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/Enumeration/{}.py".format(file_name), 'r')
    for line in file:
        line = line.split(' = ')
        line[0] = line[0].strip()
        if line[0] == variable_name:
            return line[1]


def extraction_mod(data):
    return data.replace('"', '').replace("\n", "")


def file_mod(file_name):
    return file_name.replace(" ", "")


def data_mod(data):
    return data.replace(" ", ".")


def get_data(file_name, heading, variable):
    config = configparser.RawConfigParser()
    config.read(file_name)
    return config.get(heading, variable)


def json_data(file_name, path_variable):
    with open('{}{}.json'.format(file_name, path_variable)) as file:
        data = json.load(file)
    return data

# def json_data_appium(file_name):
#     with open('C:/Users/msibtain.haider/Desktop/Python_Automation1/tests/Android/{}.json'.format(file_name)) as file:
#         data = json.load(file)
#     return data
