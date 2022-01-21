import json
import csv
import os
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib3 
from webdriverFrameworkCorePython.src.main.webdriver.core import WebDriverFactory


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
factory = WebDriverFactory.WebDriverFactoryClass.getInstance()

user_data = '../../data/user.csv'
product_data = '../../data/product.csv'

def combine_dict(dict1, dict2):
    dict_1 = json.loads(str(dict1))
    dict_2 = json.loads(str(dict2))

    dict_1.update(dict_2)

    return dict_1

def get_endpoint():
    url_to_test = factory.getTestEndpoint()
    return url_to_test

def get_caps_single():

    allPlatforms = factory.getPlatforms()

    single_caps = factory.getPlatformCaps(allPlatforms[0], "Robot Test", None)
    return single_caps

def get_test_endpoint():

    testendpoint = factory.getTestEndpoint()

    return testendpoint


def get_row_item_from_file(filepath, key):

    dirname = os.path.dirname(__file__)
    filename = os.path.normpath(os.path.join(dirname, filepath))

    with open(filename, 'r') as data:
        for line in csv.reader(data):
            if line[0] == key:
                return line[1]


def get_password(username):

    password = get_row_item_from_file(user_data, username)
    return password


def get_product_prices():
    dirname = os.path.dirname(__file__)
    filename = os.path.normpath(os.path.join(
        dirname, product_data))

    prices = []
    with open(filename, 'r') as data:
        for line in csv.reader(data):
            if line[3] != 'price':
                prices.append(int(line[3]))

    prices = sorted(prices)

    for i in range(0, len(prices)):
        prices[i] = str('$' + str(prices[i]) + '.00')

    return prices


def set_loc(lat, long):

    global se2lib

    se2lib.driver.execute_script(
        "navigator.geolocation.getCurrentPosition = function(cb){cb({ coords: {accuracy: 20,altitude: null,altitudeAccuracy: null,heading: null,latitude: " + lat + ",longitude: " + long + ",speed: null}}); }")
    se2lib.driver.execute_script(
        "window.navigator.geolocation.getCurrentPosition = function(cb){cb({ coords: {accuracy: 20,altitude: null,altitudeAccuracy: null,heading: null,latitude: " + lat + ",longitude: " + long + ",speed: null}}); }")


def mark_test_session(result):
    global se2lib

    if result == 'PASS':
        se2lib.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Ran Succesfully"}}')
    else:
        se2lib.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Oops! my sample test failed"}}')


def set_session_name(new_name):
    global se2lib
    se2lib.driver.execute_script(
        'browserstack_executor: {"action": "setSessionName", "arguments": {"name": "' + new_name + '"}}')
