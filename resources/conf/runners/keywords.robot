*** Settings ***
Library  Library.py

*** Variables ***
${caps_path}     ${CURDIR}/../../../../browserstack-examples-robot/resources/conf/caps/test_caps.json


*** Keywords ***
Start Test
    [Arguments]   ${testType}
    # Run Keyword If  '${testType}'=='single'    Start single Test    ELSE    Start local Test

    Run Keyword If    '${testType}'=='single'    Start single Test    ELSE IF    '${testType}'=='local'    Start local Test        ELSE IF    '${testType}'=='docker'    Start docker Test    ELSE    Start prem Test


Start single Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['application_endpoint']}
    ${user}=    Set Variable     ${json_object2['user']}
    ${access_key}=    Set Variable     ${json_object2['key']}

    ${caps}=    get_caps_single    ${caps_path}

    Open Browser    ${application_endpoint}    remote_url=http://${user}:${access_key}@hub-cloud.browserstack.com/wd/hub    desired_capabilities=${caps}
    # Open Browser    ${application_endpoint}    Firefox    remote_url=http://localhost:4444/wd/hub

# http://selenium_hub:4444/wd/hub
Start local Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['tests']['local']['application_endpoint']}
    ${user}=    Set Variable     ${json_object2['user']}
    ${access_key}=    Set Variable     ${json_object2['key']}

    ${caps}=    get_caps_local    ${caps_path}

    ${local_instance}=    start_local    ${access_key}

    Open Browser    ${application_endpoint}    remote_url=http://${user}:${access_key}@hub-cloud.browserstack.com/wd/hub    desired_capabilities=${caps}

    # [return]  ${local_instance}

Stop Local Test
    stop_local


Start prem Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['application_endpoint']}


    Open Browser    ${application_endpoint}   chrome


Start docker Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['application_endpoint']}

    Open Browser    ${application_endpoint}    chrome    remote_url=http://localhost:4444/wd/hub


Stop Test
    [Arguments]   ${testType}
    Run Keyword If  '${testType}'=='local'    stop_local
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

Rename Session
    [Arguments]   ${new_name}
    set_session_name    ${new_name}