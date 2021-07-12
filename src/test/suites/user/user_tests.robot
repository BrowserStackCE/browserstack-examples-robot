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
# Test case 5
Check Login with image_not_loading_user

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    Check image_not_loading_user

    Login.Login    image_not_loading_user    testingisfun99

    Check If Username Is    image_not_loading_user

    [Teardown]    Stop Test    ${testType}

# Test Case 6
Check Order in existing_orders_user

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    Check existing_orders_user

    Login.Login    existing_orders_user    testingisfun99

    Click On Orders
    Confirm Order Greater Than Zero

    [Teardown]    Stop Test    ${testType}

# Test Case 7
Add fav and check fav count

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    Check Fav

    Login.Login    existing_orders_user    testingisfun99

    Favourites.Add Item To Fav

    HomePage.Click On Favourites

    Favourites.Confirm Favourites Greater Than Zero

    [Teardown]    Stop Test    ${testType}

