import json
import pyautogui as py
import configparser
import os

current_script_path = os.path.abspath(__file__)
root_dir = os.path.dirname(current_script_path)


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
    file = open(root_dir + "/Enumeration/{}.py".format(file_name), 'r')
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


def json_data_assigning(variable, value, json_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    json_data[variable] = value
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


def json_data_removal(variable, json_file_path):
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    json_data[variable] = ''
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


def json_data_get(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data


def properties_file_updater(file_name, section, variable, to_value):
    config = configparser.RawConfigParser()
    config.read(file_name)
    cfgfile = open(file_name, 'w')
    config.set(section, variable, to_value)
    config.write(cfgfile)
    cfgfile.close()
