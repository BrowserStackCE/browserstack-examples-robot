from browserstack.local import Local
import json
import csv
import os

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
