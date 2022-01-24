*** Settings ***
Library    Library.py


*** Keywords ***
Start Test
    [Arguments]    ${testType}

    Run Keyword If    '${testType}'=='bstack-single'    Start single Test       ELSE IF    '${testType}'=='docker'    Start docker Test    ELSE    Start onprem Test


Start single Test

    ${remote_url}=    Set Variable    https://hub-cloud.browserstack.com/wd/hub

    ${application_endpoint}=    get_test_endpoint

    ${caps}=    get_caps_single    

    Open Browser    ${application_endpoint}    remote_url=${remote_url}    desired_capabilities=${caps}

Start local Test

    ${remote_url}=    Set Variable    https://hub-cloud.browserstack.com/wd/hub

    ${application_endpoint}=    get_test_endpoint

    ${caps}=    get_caps_single    

    Open Browser    ${application_endpoint}    remote_url=${remote_url}    desired_capabilities=${caps}

Start onprem Test


    ${application_endpoint}=    get_test_endpoint


    Open Browser    ${application_endpoint}    chrome


Start docker Test

    ${application_endpoint}=    get_test_endpoint

    ${docker_remote_url}=    http://localhost:4444/wd/hub

    Open Browser    ${application_endpoint}    chrome    remote_url=${docker_remote_url}


Stop Test
    [Arguments]    ${testType}

    Only Run On Browserstack    Mark Test Status                 ${TEST_STATUS}
    Close Browser

Get Password From CSV
    [Arguments]    ${username}
    ${password}    get_password    ${username}
    [return]       ${password}

Set Location
    [Arguments]    ${lat}    ${long}
    set_loc        ${lat}    ${long}


Mark Test Status
    [Arguments]          ${status}
    mark_test_session    ${status}


Rename Session
    [Arguments]         ${new_name}
    set_session_name    ${new_name}

Only Run On Browserstack
    [Arguments]       ${keyword}                        ${param}
    Run Keyword If    '${testType}'=='bstack-single'    ${keyword}    ${param}

Get Product Prices From CSV
    ${prices}=    get_product_prices
    [return]      ${prices}