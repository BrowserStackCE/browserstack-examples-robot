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
    Start Test

    Click On Favourites

    On Signin Page
    
    Stop Test

#Test Case 4
Check Login with locked_user
    
    Start Test

    Login.Login    locked_user    testingisfun99

    Confirm Locked User Error

    Stop Test
