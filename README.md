![Logo](https://www.browserstack.com/images/static/header-logo.jpg)

# BrowserStack Examples Robot Framework 
<a href="https://robotframework.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Robot-framework-logo.png" alt="Robot" height="30" /></a> 
<a href="https://www.python.org/"><img src="https://www.python.org/static/img/python-logo@2x.png" alt="Python" height="22" /></a>

## Introduction

Robot Framework is a generic open source automation framework that is used for test automation. It is open and extensible, and can be integrated with many tools to create powerful and flexible automation solutions. Robot Framework has an easy syntax, utilizing human-readable keywords, and its capabilities can be extended through libraries implemented in Python or Java.

This BrowserStack Example repository demonstrates a Selenium test framework written in Robot Framework with parallel testing capabilities. The Selenium test scripts are written for the open source [BrowserStack Demo web application](https://bstackdemo.com) ([Github](https://github.com/browserstack/browserstack-demo-app)). This BrowserStack Demo App is an e-commerce web application that showcases multiple real-world user scenarios. The app is bundled with offers data, orders data, and products data, containing everything you need to start using the app and run tests out-of-the-box.

The Selenium tests in this repo are run on BrowserStack's real device/browser using various run configurations and test capabilities.

---

# BrowserStack

[BrowserStack](https://browserstack.com) provides instant access to 3,000+ real mobile devices and browsers on a highly reliable cloud infrastructure that effortlessly scales as testing needs grow.

## Repository Setup

- Clone the repository:
    ```sh
    git clone https://github.com/BrowserStackCE/browserstack-examples-robot.git
    ```

### Using Python 3.8 or Above with Pipenv

This project requires Python version 3.8 or higher. Robot Framework requires Python 3.8 or newer. The latest version that supports Python 3.6 and 3.7 is Robot Framework 6.1.1. If you need to use Python 2, Jython, or IronPython, you can use Robot Framework 4.1.3. 

If you do not have a compatible Python version installed, please follow these steps:

1. **Install Python 3.8 or Higher**:
   - Download and install Python 3.8 or a higher version from the official Python website: https://www.python.org/downloads/
   - Ensure that the installed Python version is added to your system's PATH.

2. **Install and Set Up Pipenv**:
   - Install Pipenv using:
     ```
     pip install pipenv
     ```
   - Create a Pipenv environment specifically for Python 3.8 or higher:
     ```
     pipenv --python 3.8
     ```
   - Activate the Pipenv environment:
     ```
     pipenv shell
     ```
   - Verify the Python version:
     ```
     python --version
     ```
     It should display Python 3.8.x or higher.

3. **Install Dependencies**:
   - Install the required dependencies in your Pipenv environment by running:
     ```
     pipenv install
     ```
   - This installs all the dependencies listed in the `Pipfile`.

## About the Tests in This Repository

This repository contains the following Selenium tests:

| Module   | Test Name                          | Description |
| ---      | ---                                | ---         |
| e2e      | E2E Test                           | This test scenario verifies the successful product purchase lifecycle from end to end. It demonstrates the [Page Object Model design pattern](https://www.browserstack.com/guide/page-object-model-in-selenium) and is also the default test executed in all the single test run profiles. |
| login    | Check if Signin opens on clicking on favourites nav item | This test verifies the login workflow with different types of valid login users. |
| login    | Check Login with locked_user       | This test verifies the login workflow error for a locked user. |
| offers   | Set GPS location to Mumbai and check offers | This test mocks the GPS location to Mumbai and verifies that the applicable product offers for this location are displayed. |
| product  | Apply Apple And Samsung Filter     | This test verifies that the Apple products are only shown if the Apple vendor filter option is applied. |
| product  | Apply 'Lowest to Highest' Order By Filter | This test verifies that the product prices are in ascending order when the product sort "Lowest to Highest" is applied. |
| user     | Check Login with image_not_loading_user | This test verifies that the product images load for user: "image_not_loading_user" on the e-commerce application. Since the images do not load, the test case assertion fails.|
| user     | Check Order in existing_orders_user | This test verifies that existing orders are shown for user: "existing_orders_user". |

---

## Running Your Tests on an On-Prem Browser

### Running a Single Test on an On-Prem Browser

To execute a single test, run the below command: 
```sh
robot /path/to/test.robot
```
For example: 
```sh
robot ./src/test/suites/e2e/e2e.robot
```

### Running Parallel Tests on On-Prem Browsers 

To execute parallel tests, run the below command: 
```sh
pabot path/to/testsuiteFolder
```
For example: 
```sh
pabot ./src/test/suites
```

## Running Your Tests on BrowserStack

### Prerequisites to Run Your Tests on BrowserStack

- Create a new [BrowserStack account](https://www.browserstack.com/users/sign_up) or use an existing one.
- Identify your BrowserStack username and access key from the [BrowserStack Automate Dashboard](https://automate.browserstack.com/) and export them as environment variables using the below commands.

    - For \*nix based and Mac machines:

    ```sh
    export BROWSERSTACK_USERNAME=<browserstack-username> &&
    export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```

    - For Windows:

    ```shell
    set BROWSERSTACK_USERNAME=<browserstack-username>
    set BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
    ```
  
  Alternatively, you can hardcode the username and access_key in the `browserstack.yml` SDK file. 

Note:
- You can use the [BrowserStack SDK Configurator](https://www.browserstack.com/docs/automate/selenium/sdk-config-generator) to create your `browserstack.yml` file and update it based on your device/browser test requirements.

### Run a Specific Test

- How to run the test?

  To run a specific test scenario, use the command below:
  
  ```sh
  browserstack-sdk robot /path/to/test.robot
  ```

- Output

  This run profile executes the specific test scenario on BrowserStack on the platforms configured in your `browserstack.yml` file.

### Run the Entire Test Suite

- How to run the test?

  To run the entire test suite in parallel on BrowserStack, you will require the [pabot dependency](https://pabot.org/). Use the following command:
  
  ```sh
  browserstack-sdk pabot path/to/testsuiteFolder
  ```
  You can also use other combinations as described in [pabot](https://pabot.org/) to run your tests in parallel.

- Output

  This run profile executes the entire test suite in parallel on BrowserStack on the platforms configured in your `browserstack.yml` file. 

---

### Run Tests on BrowserStack That Require Local Environment Access

The only required change is to add the respective options in the `browserstack.yml` file. The browserstack-sdk handles the starting and termination of the BrowserStack Local Instance.

`browserstackLocal: true`

browserstackLocal is set to true in this repo.

## Additional Resources

- View your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate).
- Customize your test capabilities on BrowserStack using our [SDK Configurator](https://www.browserstack.com/docs/automate/selenium/sdk-config-generator).
- [List of Browsers & Mobile Devices](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate) for automation testing on BrowserStack.
- [Using the Automate REST API](https://www.browserstack.com/automate/rest-api) to access information about your tests via the command-line interface.
- Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github).
- For testing public web applications behind IP restriction, [Inbound IP Whitelisting](https://www.browserstack.com/local-testing/inbound-ip-whitelisting) can be enabled with the [BrowserStack Enterprise](https://www.browserstack.com/enterprise) offering.
