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

*** Variables ***
${testType}    single


*** Test Cases ***
# Test Case 1
Apply 'Lowest to Highest' Order By Filter

    Start Test  ${testType}

    Select Lowest To Highest Filter

    Check If Product Sorted

    Sleep   2


    Close All Browsers

# Test Case 2
Apply Apple And Samsung Filter

    Start Test  ${testType}

    ${total_elements_before}=  Get Total Products

    Select Filter   Apple
    Select Filter   Samsung

    Check If Total Product Changed  ${total_elements_before}

    Sleep   3
    Close All Browsers
