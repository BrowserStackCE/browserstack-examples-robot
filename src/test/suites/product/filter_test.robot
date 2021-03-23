*** Settings ***
Library  SeleniumLibrary
Library  Collections
Library  OperatingSystem
Library  String

Resource  ${CURDIR}/../../../../resources/conf/runners/keywords.robot
Resource  ${CURDIR}/../../../app/pages/Login.robot
Resource  ${CURDIR}/../../../app/pages/Checkout.robot
Resource  ${CURDIR}/../../../app/pages/HomePage.robot
Resource  ${CURDIR}/../../../app/pages/Confirmation.robot
Resource  ${CURDIR}/../../../app/pages/Favourites.robot


*** Test Cases ***
# Test Case 1
Apply 'Lowest to Highest' Order By Filter

    Start Test  ${testType}

    Run Keyword If    '${testType}'=='single'    Rename Session  Apply Filter    ELSE IF    '${testType}'=='local'    Rename Session  Apply Filter

    Select Lowest To Highest Filter

    Check If Product Sorted

    Run Keyword If    '${testType}'=='single'    Mark Test Pass    ELSE IF    '${testType}'=='local'    Mark Test Pass

    Sleep   2
    [Teardown]   Stop Test  ${testType}

# Test Case 2
Apply Apple And Samsung Filter

    Start Test  ${testType}

    Run Keyword If    '${testType}'=='single'    Rename Session  Apply Filter    ELSE IF    '${testType}'=='local'    Rename Session  Apply Filter

    ${total_elements_before}=  Get Total Products

    Select Filter   Apple
    Select Filter   Samsung

    Check If Total Product Changed  ${total_elements_before}

    Run Keyword If    '${testType}'=='single'    Mark Test Pass    ELSE IF    '${testType}'=='local'    Mark Test Pass

    Sleep   3
    [Teardown]   Stop Test  ${testType}
