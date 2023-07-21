import pyautogui as py


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
    file = open("{}.py".format(file_name), 'r')
    for line in file:
        line = line.split(' = ')
        line[0] = line[0].strip()
        if line[0] == variable_name:
            return line[1]
