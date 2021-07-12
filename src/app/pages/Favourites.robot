*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Confirm Favourites Greater Than Zero
    Wait Until Element Is Visible   class=shelf-item
    ${favs}=     Get Element Count    class=shelf-item
    Should Be True  ${favs} > 0

Add Item To Fav
    Wait Until Element Is Visible   xpath=//p[text() = 'iPhone 12']/../div/button
    Click Element    xpath=//p[text() = 'iPhone 12']/../div/button
