*** Settings ***
Library    Library.py
Library    SeleniumLibrary
    
*** Keywords ***
Start Onprem Test
    Open Browser    https://bstackdemo.com/

Get Password From CSV
    [Arguments]    ${username}    
    ${password}    get_password    ${username}
    [Return]    ${password}

Set Location
    [Arguments]    ${lat}    ${long}
    set_loc    ${lat}    ${long}

Get Product Prices From CSV
    ${prices}    get_product_prices
    [Return]    ${prices}

Wait Function
    add_wait
 
Stop Test
    Close Browser
