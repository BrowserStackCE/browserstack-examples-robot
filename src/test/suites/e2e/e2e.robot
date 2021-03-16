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



*** Test Cases ***
#Test Case 8
E2E Test

    Start Test  ${testType}

    Login From CSV    fav_user



    Wait Until Element Is Visible   xpath=//p[text() = 'iPhone 12']/../div[@class = 'shelf-item__buy-btn']
    Click Element    xpath=//p[text() = 'iPhone 12']/../div[@class = 'shelf-item__buy-btn']
    Wait Until Element Is Visible   class=float-cart__close-btn
    Click Element   class=float-cart__close-btn

    Click Element    xpath=//p[text() = 'iPhone XS']/../div[@class = 'shelf-item__buy-btn']
    Wait Until Element Is Visible   class=float-cart__close-btn
    Click Element   class=float-cart__close-btn

    Click Element    xpath=//p[text() = 'Galaxy S20']/../div[@class = 'shelf-item__buy-btn']
    Wait Until Element Is Visible   class=float-cart__close-btn
    Click Element   class=buy-btn


    Checkout With Dummy Data

    
    Continue Shopping

    Click On Orders

    Item In Orders Should Be Equal To   3

    Sleep   3

    Stop Test  ${testType}


