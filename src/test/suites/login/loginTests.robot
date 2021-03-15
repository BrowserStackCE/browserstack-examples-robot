*** Settings ***
Library  SeleniumLibrary
Library  Collections
Library  OperatingSystem
Library  String

Resource  ${EXECDIR}/../../../../resources/conf/runners/keywords.robot
Resource  ${EXECDIR}/../../../app/pages/Login.robot
Resource  ${EXECDIR}/../../../app/pages/Checkout.robot
Resource  ${EXECDIR}/../../../app/pages/HomePage.robot
Resource  ${EXECDIR}/../../../app/pages/Confirmation.robot
Resource  ${EXECDIR}/../../../app/pages/Favourites.robot


*** Test Cases ***
#Test Case 3
Check if Signin opens on clicking on favourites nav item 

    Start Test  ${testType}

    Click On Favourites

    Sleep   1

    On Signin Page

    Sleep    3   

    Close All Browsers


#Test Case 4
Check Login with locked_user

    Start Test  ${testType}
    Login.Login  locked_user  testingisfun99
    
    Confirm Locked User Error

    Sleep    3
    Close Browser
