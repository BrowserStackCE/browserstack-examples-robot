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
#Test Case 9
Set GPS location to Mumbai and check offers

    Start Test  ${testType}

    Set Location    19.043192    72.86305240000002

    Login From CSV    fav_user

    Click On Offers

    Confirm Offers Greater Than Zero

    Sleep   3
    Stop Test  ${testType}

