*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Perform Order Checkout

    Wait Until Element Is Visible   id=firstNameInput
    Input Text  id=firstNameInput   firstname
    Input Text  id=lastNameInput   lastname
    Input Text  id=addressLine1Input   address
    Input Text  id=provinceInput   state
    Input Text  id=postCodeInput   12345

    Click Element   id=checkout-shipping-continue

Continue Shopping
    Wait Until Element Is Visible   class=button--tertiary
    Click Element   class=button--tertiary
