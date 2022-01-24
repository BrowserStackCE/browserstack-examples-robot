*** Settings ***
Library  SeleniumLibrary

Resource  ${CURDIR}/../../../resources/conf/runners/keywords.robot

*** Keywords ***
Login
    [Arguments]   ${username}   ${password}

    Wait Until Element Is Visible   id=signin
    Click Element   id=signin

    Wait Until Element Is Visible   id=username
    Press Keys    id=username    ${username}
    Press Keys    None    ENTER
    Press Keys    id=password    ${password}
    Press Keys    None    ENTER
    Press Keys    None    ENTER

Login From CSV
    [Arguments]   ${username}

    Wait Until Element Is Visible   id=signin
    Click Element   id=signin

    Wait Until Element Is Visible   id=username
    Press Keys    id=username    ${username}
    Press Keys    None    ENTER

    ${password}=    keywords.Get Password From CSV  ${username}
    Press Keys    id=password    ${password}
    Press Keys    None    ENTER
    Press Keys    None    ENTER
