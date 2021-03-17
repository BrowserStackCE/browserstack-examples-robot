*** Settings ***
Library  Library.py

*** Variables ***
${caps_path}     ${EXECDIR}/../../../../resources/conf/caps/test_caps.json


*** Keywords ***

Start Test
    [Arguments]   ${error_status}
    Run Keyword If  '${error_status}'=='single'    Start single Test    ELSE    Start local Test


Start single Test

    ${json2}=    Get file    ${caps_path}
    ${json_object2}=    Evaluate    json.loads('''${json2}''')    json


    ${application_endpoint}=    Set Variable     ${json_object2['application_endpoint']}
    ${user}=    Set Variable     ${json_object2['user']}
    ${access_key}=    Set Variable     ${json_object2['key']}

    ${caps}=    get_caps_single    ${caps_path}

    Open Browser    ${application_endpoint}    remote_url=http://${user}:${access_key}@hub-cloud.browserstack.com/wd/hub    desired_capabilities=${caps}


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
