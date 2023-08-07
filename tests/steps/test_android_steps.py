from appium import webdriver

desired_cap = {
    "deviceName": "",
    "platformName": "Android",
    "app": ""
}

driver = webdriver.Remote("https:://localhost:4723", desired_cap)
