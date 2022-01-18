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
# Test Case 1
Apply 'Lowest to Highest' Order By Filter

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    Apply Filter

    Select Lowest To Highest Filter

    Check If Product Sorted

    [Teardown]    Stop Test    ${testType}

# Test Case 2
Apply Apple And Samsung Filter

    Start Test    ${testType}

    Only Run On Browserstack    Rename Session    Apply Filter

    ${total_elements_before}=    Get Total Products

    Select Filter    Apple
    Select Filter    Samsung

    Check If Total Product Changed    ${total_elements_before}

    [Teardown]    Stop Test    ${testType}
