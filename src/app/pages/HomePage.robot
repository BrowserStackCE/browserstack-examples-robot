*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Click On Orders
    Wait Until Element Is Visible   id=orders
    Click Element   id=orders
    Wait Until Element Is Visible   class=order

Click On Favourites
    Wait Until Element Is Visible   id=favourites
    Click Element   id=favourites

Click On Offers
    Wait Until Element Is Visible   id=offers
    Click Element   id=offers

Check If Username Is
    [Arguments]   ${username}
    Wait Until Element Is Visible   class=username
    Element Text Should Be    class=username    ${username}


Select Lowest To Highest Filter
    Wait Until Element Is Visible   class=sort
    Click Element   class=sort

    Click Element   css= option[value='lowestprice']

Check If Product Sorted
    Wait Until Element Is Visible   class=val

    @{elem} =   Get WebElements     class=val

    @{HOMEPAGE_PRICE_LIST}=  Create List

    FOR  ${item}  IN  @{elem}
        ${text}=    Get Text    ${item}
        Append To List  ${HOMEPAGE_PRICE_LIST}    ${text}
    END

    ${prices}=    Get Product Prices From CSV

    Lists Should Be Equal   ${HOMEPAGE_PRICE_LIST}   ${prices}

Get Total Products
    Wait Until Element Is Visible   css=input[value='Apple'] + span
    ${total_elements}=  Get Text  class=products-found

    [return]  ${total_elements}

Select Filter
    [Arguments]   ${filter}
    Click Element   css=input[value='${filter}'] + span


Check If Total Product Changed
    [Arguments]   ${total_elements_before}
    Element Text Should Not Be   class=products-found   ${total_elements_before}

