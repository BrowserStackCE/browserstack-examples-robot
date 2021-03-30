*** Settings ***
Library  Library.py

*** Variables ***
${caps_path}     ${CURDIR}/../../../../browserstack-examples-robot/resources/conf/caps/test_caps.json


*** Keywords ***
Start Test
    [Arguments]   ${testType}

    Run Keyword If    '${testType}'=='bstack-single'    Start single Test    ELSE IF    '${testType}'=='bstack-local'    Start local Test        ELSE IF    '${testType}'=='docker'    Start docker Test    ELSE    Start onprem Test


Start single Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['application_endpoint']}

    ${username_status}    Run Keyword And Return Status    Get Environment Variable    BROWSERSTACK_USERNAME
    ${acess_key_status}    Run Keyword And Return Status    Get Environment Variable    BROWSERSTACK_ACCESS_KEY

    ${user}=      Set Variable If    """${username_status}""" == 'True'    %{BROWSERSTACK_USERNAME}    ${json_object2['user']} 
    ${access_key}=      Set Variable If    """${acess_key_status}""" == 'True'    %{BROWSERSTACK_ACCESS_KEY}    ${json_object2['key']} 

    ${caps}=    get_caps_single    ${caps_path}

    Open Browser    ${application_endpoint}    remote_url=http://${user}:${access_key}@hub-cloud.browserstack.com/wd/hub    desired_capabilities=${caps}

Start local Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['tests']['local']['application_endpoint']}

    ${username_status}    Run Keyword And Return Status    Get Environment Variable    BROWSERSTACK_USERNAME
    ${acess_key_status}    Run Keyword And Return Status    Get Environment Variable    BROWSERSTACK_ACCESS_KEY

    ${user}=      Set Variable If    """${username_status}""" == 'True'    %{BROWSERSTACK_USERNAME}    ${json_object2['user']} 
    ${access_key}=      Set Variable If    """${acess_key_status}""" == 'True'    %{BROWSERSTACK_ACCESS_KEY}    ${json_object2['key']} 


    ${caps}=    get_caps_local    ${caps_path}

    ${local_instance}=    start_local    ${access_key}

    Open Browser    ${application_endpoint}    remote_url=http://${user}:${access_key}@hub-cloud.browserstack.com/wd/hub    desired_capabilities=${caps}


Stop Local Test
    stop_local


Start onprem Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['application_endpoint']}


    Open Browser    ${application_endpoint}   chrome


Start docker Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['application_endpoint']}

    ${docker_remote_url}=    http://localhost:4444/wd/hub
    
    Open Browser    ${application_endpoint}    chrome    remote_url=${docker_remote_url}


Stop Test
    [Arguments]   ${testType}

    Log   ${TEST_STATUS}
    
    Run Keyword If    '${testType}'=='bstack-single'    Mark Test Status   ${TEST_STATUS}    ELSE IF    '${testType}'=='bstack-local'    Mark Test Status   ${TEST_STATUS}

    Run Keyword If  '${testType}'=='bstack-local'    stop_local
    Close Browser


Get Password From CSV
    [Arguments]   ${username}
    ${password}   get_password   ${username}
    [return]  ${password}

Set Location
        [Arguments]   ${lat}    ${long}
        set_loc   ${lat}    ${long}

Mark Test Pass
    mark_pass

Mark Test Fail
    mark_fail

Mark Test Status
    [Arguments]   ${status}
    mark_test_session   ${status}


Rename Session
    [Arguments]   ${new_name}
    set_session_name    ${new_name}