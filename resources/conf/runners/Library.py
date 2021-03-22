from browserstack.local import Local
import json
import csv
import os
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


bs_local = 0

def combine_dict(dict1, dict2):
    dict_1 = json.loads(str(dict1))
    dict_2 = json.loads(str(dict2))

    dict_1.update(dict_2)

    return dict_1


def get_caps_single(caps_path):

    with open(caps_path) as f:
        data = json.load(f)

    single_caps_common = data['tests']['single']['common_caps']
    single_caps_env = data['tests']['single']['env_caps'][0]

    single_caps_common.update(single_caps_env)


    return single_caps_common

def get_caps_local(caps_path):

    with open(caps_path) as f:
        data = json.load(f)

    caps_common = data['tests']['local']['common_caps']
    caps_env = data['tests']['local']['env_caps'][0]

    caps_common.update(caps_env)


    return caps_common

def start_local(key):

    global bs_local
    bs_local = Local()


    bs_local_args = { "key": key }

    bs_local.start(**bs_local_args)

    return bs_local

def stop_local():

    global bs_local

    bs_local.stop()


def get_password(username):

    dirname = os.path.dirname(__file__)

    filename = os.path.normpath(os.path.join(dirname, '../../data/user.csv'))

    print(filename)

    with open(filename,'r') as data: 
        for line in csv.reader(data): 
                    # print(line)
                    if line[0] == username:
                        return line[1]


def set_loc(lat, long):

    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    # se2lib.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Oops! my sample test failed"}}')


    se2lib.driver.execute_script(
        "navigator.geolocation.getCurrentPosition = function(cb){cb({ coords: {accuracy: 20,altitude: null,altitudeAccuracy: null,heading: null,latitude: " + lat + ",longitude: " + long + ",speed: null}}); }"
        )
    se2lib.driver.execute_script(
        "window.navigator.geolocation.getCurrentPosition = function(cb){cb({ coords: {accuracy: 20,altitude: null,altitudeAccuracy: null,heading: null,latitude: " + lat + ",longitude: " + long + ",speed: null}}); }"
        )

def mark_pass():
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason": "Test Ran Succesfully"}}')

def mark_fail():
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed","reason": "Oops! my sample test failed"}}')


def set_session_name(new_name):
    se2lib = BuiltIn().get_library_instance('SeleniumLibrary')
    se2lib.driver.execute_script('browserstack_executor: {"action": "setSessionName", "arguments": {"name": "' + new_name + '"}}')

