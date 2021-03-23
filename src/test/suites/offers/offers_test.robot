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
#Test Case 9
Set GPS location to Mumbai and check offers

    keywords.Start Test  ${testType}

    Run Keyword If    '${testType}'=='single'    Rename Session  Check Offers Test    ELSE IF    '${testType}'=='local'    Rename Session  Check Offers Test

    Set Location    19.043192    72.86305240000002

    Login From CSV    fav_user

    Click On Offers

    Confirm Offers Greater Than Zero

    Run Keyword If    '${testType}'=='single'    Mark Test Pass    ELSE IF    '${testType}'=='local'    Mark Test Pass

    Sleep   3
    [Teardown]   Stop Test  ${testType}

