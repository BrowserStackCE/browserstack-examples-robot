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
#Test Case 8
E2E Test

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    E2E

    Login From CSV    fav_user

    Wait Until Element Is Visible    css=div[id="1"]>div[class="shelf-item__buy-btn"] 
    Click Element                    css=div[id="1"]>div[class="shelf-item__buy-btn"] 
    Wait Until Element Is Visible    class=float-cart__close-btn
    Click Element                    class=float-cart__close-btn

    Click Element                    css=div[id="7"]>div[class="shelf-item__buy-btn"]
    Wait Until Element Is Visible    class=float-cart__close-btn
    Click Element                    class=float-cart__close-btn

    Click Element                    css=div[id="10"]>div[class="shelf-item__buy-btn"]
    Wait Until Element Is Visible    class=float-cart__close-btn
    Click Element                    class=buy-btn

    Perform Order Checkout

    Continue Shopping

    Click On Orders

    Item In Orders Should Be Equal To    3

    [Teardown]    Stop Test    ${testType}


