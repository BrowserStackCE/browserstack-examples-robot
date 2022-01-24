*** Settings ***
Library    SeleniumLibrary
Library    Collections
Library    OperatingSystem
Library    String

Resource    ${CURDIR}/../../../../resources/conf/runners/keywords.robot
Resource    ${CURDIR}/../../../app/pages/Login.robot
Resource    ${CURDIR}/../../../app/pages/Checkout.robot
Resource    ${CURDIR}/../../../app/pages/HomePage.robot
Resource    ${CURDIR}/../../../app/pages/Confirmation.robot
Resource    ${CURDIR}/../../../app/pages/Favourites.robot


*** Test Cases ***
#Test Case 3
Check if Signin opens on clicking on favourites nav item

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    Check Signin

    Click On Favourites

    On Signin Page

    [Teardown]    Stop Test    ${testType}


#Test Case 4
Check Login with locked_user

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    Check locked_user

    Login.Login    locked_user    testingisfun99

    Confirm Locked User Error

    [Teardown]    Stop Test    ${testType}
