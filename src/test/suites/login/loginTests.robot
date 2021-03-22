*** Settings ***
Library  SeleniumLibrary
Library  Collections
Library  OperatingSystem
Library  String

Resource  ${CURDIR}/../../../../resources/conf/runners/keywords.robot
Resource  ${CURDIR}/../../../app/pages/Login.robot
Resource  ${CURDIR}/../../../app/pages/Checkout.robot
Resource  ${CURDIR}/../../../app/pages/HomePage.robot
Resource  ${CURDIR}/../../../app/pages/Confirmation.robot
Resource  ${CURDIR}/../../../app/pages/Favourites.robot


*** Test Cases ***
#Test Case 3
Check if Signin opens on clicking on favourites nav item 

    Start Test  ${testType}

    Rename Session  Check Favourites

    Click On Favourites

    Sleep   1

    On Signin Page

    Mark Test Pass

    Sleep    3   

    [Teardown]   Stop Test  ${testType}


#Test Case 4
Check Login with locked_user

    Start Test  ${testType}

    Rename Session  Check locked_user

    Login.Login  locked_user  testingisfun99
    
    Confirm Locked User Error

    Mark Test Pass

    Sleep    3
    [Teardown]   Stop Test  ${testType}
