![Logo](https://www.browserstack.com/images/static/header-logo.jpg)

# BrowserStack Examples Robot Framework <a href="https://robotframework.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Robot-framework-logo.png" alt="Robot" height="30" /></a> <a href="https://www.python.org//"><img src="https://www.python.org/static/img/python-logo@2x.png" alt="python" height="22" /></a>

## Introduction

Robot Framework is a generic open source automation framework which can be used for test automation. It is open and extensible and can be integrated with many tools to create powerful and flexible automation solutions.
Robot Framework has easy syntax, utilising human-readable keywords and its capabilities can be extended by libraries implemented with Python or Java.

This BrowserStack Example repository demonstrates a Selenium test framework written in Robot Framework with parallel testing capabilities. The Selenium test scripts are written for the open source [BrowserStack Demo web application](https://bstackdemo.com) ([Github](https://github.com/browserstack/browserstack-demo-app)). This BrowserStack Demo App is an e-commerce web application which showcases multiple real-world user scenarios. The app is bundled with offers data, orders data and products data that contains everything you need to start using the app and run tests out-of-the-box.

The Selenium test tests are run on different platforms like on-prem, docker and BrowserStack using various run configurations and test capabilities.

---

## Repository setup

- Clone the repository

- Ensure you have the following dependencies installed on the machine
    - Python 3

    Install the requirements:
    ```sh
    pip install -r requirements.txt
    ```


## About the tests in this repository

  This repository contains the following Selenium tests:

  | Module   | Test name                          | Description |
  | ---   | ---                                   | --- |
  | e2e      | E2E Test                | This test scenario verifies successful product purchase lifecycle end-to-end. It demonstrates the [Page Object Model design pattern](https://www.browserstack.com/guide/page-object-model-in-selenium) and is also the default test executed in all the single test run profiles. |
  | login    | Check if Signin opens on clicking on favourites nav item          | This test verifies the login workflow with different types of valid login users. |
  | login    | Check Login with locked_user               | This test verifies the login workflow error for a locked user. |
  | offers   | Set GPS location to Mumbai and check offers     | This test mocks the GPS location for Mumbai and verifies that the product offers applicable for the Mumbai location are shown.   |
  | product  | Apply Apple And Samsung Filter          | This test verifies that the Apple products are only shown if the Apple vendor filter option is applied. |
  | product  | Apply 'Lowest to Highest' Order By Filter   | This test verifies that the product prices are in ascending order when the product sort "Lowest to Highest" is applied. |
  | user     | Check Login with image_not_loading_user | This test verifies that the product images load for user: "image_not_loading_user" on the e-commerce application. Since the images do not load, the test case assertion fails.|
  | user     | Check Order in existing_orders_user |  This test verifies that existing orders are shown for user: "existing_orders_user"  |
  
  ---


## Test infrastructure environments 

- [On-premise/self-hosted](#on-premise-self-hosted)
- [Docker](#docker)
- [BrowserStack](#browserstack)


## Configuring the maximum parallel test threads for this repository

  For all the parallel run configuration profiles, you can configure the maximum parallel test threads by changing the settings below.

  - Docker / BrowserStack

    While running any of the below tests in parallel, set the maximum parallel thread using the pabot argument as below:

    `pabot --processes <count_of_parallels> <name_of_suites_to_run>`
  
  
## Test Reporting

- [Allure reports](#generating-allure-reports)

---

# On Premise / Self Hosted

This infrastructure points to running the tests on your own machine using a browser (e.g. Chrome) using the browser's driver executables (e.g. ChromeDriver for Chrome). #{ Selenium enables this functionality using WebDriver for many popular browsers.}

## Prerequisites

- For this infrastructure configuration (i.e on-premise), ensure that the ChromeDriver executable is placed in the `/src/test/resources/drivers` folder.

Note: The ChromeDriver version must match the Chrome browser version on your machine.

## Running Your Tests

### Run a specific test on your own machine

- How to run the test?

  To run a specific test scenario, use the following command with the additional 'test-name' argument:
  
  ```sh
  robot --variable testType:on-prem --test "<Test scenario name>" . 
  ```


  where,  the argument 'test-name' can be any RobotFramework scenario name configured in this repository.
  
  E.g. "Check Login with locked_user", "E2E Test", "Apply 'Lowest to Highest' Order By Filter" or any of the other test scenario names, as outlined in [About the tests in this repository](#About-the-tests-in-this-repository) section.

- Output

  This run profile executes a specific test scenario on a single browser instance on your own machine.


### Run the entire test suite on your own machine

- How to run the test?

  To run the entire test suite on your own machine, use the following command:
  
  ```sh
  robot --variable testType:on-prem --suite <Suite-name> .
  ```


- Output

  This run profile executes the entire test suite sequentially on a single browser, on your own machine.

  
---

# Docker

[Docker](https://docs.docker.com/get-started/overview/) is an open source platform that provides the ability to package and test applications in an isolated environment called containers.

## Prerequisites

- Install and start [Docker](https://docs.docker.com/get-docker/).
- Note: Docker should be running on the test machine. Ensure Docker Compose is installed as well.
- Run `docker-compose pull` from the current directory of the repository.

## Running Your Tests

### Run a specific test on the docker infrastructure

- How to run the test?

    - Start the Docker by running the following command:

  ```sh
  docker-compose up -d
  ```

  To run a specific test scenario, use the following command with the additional 'test-name' argument:

  ```sh
    robot --variable testType:docker --test "<Test scenario name>" . 

  ```

  
  where,  the argument 'test-name' can be any scenario name configured in this repository.
  
  E.g. "Check Login with locked_user", "E2E Test", "Apply 'Lowest to Highest' Order By Filter" or any of the other test scenario names, as outlined in [About the tests in this repository](#About-the-tests-in-this-repository) section.


  - After tests are complete, you can stop the Docker by running the following command:
      
  ```sh
  docker-compose down
  ```

- Output

  This run profile executes a specific test scenario on a single browser deployed on a docker image.


### Run the entire test suite in parallel using Docker

- How to run the test?

    - Start the docker image first by running the following command:

  ```sh
  docker-compose up -d
  ```

    - To run the entire test suite in parallel on the docker image, use the following command:

  ```sh
  robot --variable testType:docker --suite <Suite-Name> .
  ```

    - After the tests are complete stop the Selenium grid by running the following command:

  ```sh
  docker-compose down
  ```

- Output

  This run profile executes the entire test suite in parallel on a single browser, deployed on a docker image.

---

# BrowserStack

[BrowserStack](https://browserstack.com) provides instant access to 2,000+ real mobile devices and browsers on a highly reliable cloud infrastructure that effortlessly scales as testing needs grow.

## Prerequisites

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
  
  Alternatively, you can also hardcode username and access_key objects in the [test_caps.json](resources/conf/caps/test_caps.json) file.

Note:
- We have configured a list of test capabilities in the [test_caps.json](resources/conf/caps/test_caps.json) file. You can certainly update them based on your device / browser test requirements. 
- The exact test capability values can be easily identified using the [Browserstack Capability Generator](https://browserstack.com/automate/capabilities)


## Running Your Tests

### Run a specific test on BrowserStack

In this section, we will run a single test on Chrome browser on Browserstack. To change test capabilities for this configuration, please refer to the `single` object in `test_caps.json` file.

- How to run the test?
  

  To run a specific test scenario, use the following command with the additional 'test-name' argument:

  ```sh
  robot --variable testType:bstack-single --test "<Test scenario name>" . 

  ```

  where,  the argument 'test-name' can be any scenario name configured in this repository.
  
  E.g. "Check Login with locked_user", "E2E Test", "Apply 'Lowest to Highest' Order By Filter" or any of the other test scenario names, as outlined in [About the tests in this repository](#About-the-tests-in-this-repository) section.


- Output

  This run profile executes a single test on a single browser on BrowserStack. Please refer to your [BrowserStack dashboard](https://automate.browserstack.com/) for test results.


### Run the entire test suite in parallel on a single BrowserStack browser

In this section, we will run the tests in parallel on a single browser on Browserstack. Refer to `single` object in `test_caps.json` file to change test capabilities for this configuration.

- How to run the test?

  To run the entire test suite in parallel on a single BrowserStack browser, use the following command:
  
  ```sh
  pabot --testlevelsplit --variable testType:bstack-single --suite <Suite-Name> .
  ```



- Output

  This run profile executes the entire test suite in parallel on a single BrowserStack browser. Please refer to your [BrowserStack dashboard](https://automate.browserstack.com/) for test results.

  - Note: By default, this execution would run maximum 5 test threads in parallel on BrowserStack. Refer to the section ["Configuring the maximum parallel test threads for this repository"](#Configuring-the-maximum-parallel-test-threads-for-this-repository) for updating the parallel thread count based on your requirements.


### [Web application hosted on internal environment] Running your tests on BrowserStack using BrowserStackLocal

#### Prerequisites

- Clone the [BrowserStack demo application](https://github.com/browserstack/browserstack-demo-app) repository.
  ```sh
  git clone https://github.com/browserstack/browserstack-demo-app
  ``` 
- Please follow the README.md on the BrowserStack demo application repository to install and start the dev server on localhost.
- In this section, we will run a single test case to test the BrowserStack Demo app hosted on your local machine i.e. localhost. Refer to the `single_local` object in `caps.json` file to change test capabilities for this configuration.
- Note: You may need to provide additional BrowserStackLocal arguments to successfully connect your localhost environment with BrowserStack infrastructure. (e.g if you are behind firewalls, proxy or VPN).
- Further details for successfully creating a BrowserStackLocal connection can be found here:
  
  - [Local Testing with Automate](https://www.browserstack.com/local-testing/automate)
  - [BrowserStackLocal Python GitHub](https://github.com/browserstack/browserstack-local-python)


### [Web application hosted on internal environment] Run a specific test on BrowserStack using BrowserStackLocal

- How to run the test?

  To run a specific test scenario, use the following command with the additional test-name argument:

  ```sh
    robot --variable testType:bstack-local --test "<Test scenario name>" . 

  ```
  
  where,  the argument 'test-name' can be any scenario name configured in this repository.
  
  E.g. "Check Login with locked_user", "E2E Test", "Apply 'Lowest to Highest' Order By Filter" or any of the other test scenario names, as outlined in [About the tests in this repository](#About-the-tests-in-this-repository) section.


- Output

  This run profile executes a single test on an internally hosted web application on a single browser on BrowserStack. Please refer to your BrowserStack dashboard(https://automate.browserstack.com/) for test results.


### [Web application hosted on internal environment] Run the entire test suite in parallel on a single BrowserStack browser using BrowserStackLocal

In this section, we will run the test cases to test the internally hosted website in parallel on a single browser on Browserstack. Refer to the `single_local` object in `test_caps.json` file to change test capabilities for this configuration.

- How to run the test?

  To run the entire test suite in parallel on a single BrowserStack browser using BrowserStackLocal, use the following command:
  ```sh
  pabot --testlevelsplit --variable testType:bstack-local --suite <Suite-Name> .
  ```


- Output

   This run profile executes the entire test suite on an internally hosted web application on a single browser on BrowserStack. Please refer to your [BrowserStack dashboard](https://automate.browserstack.com/) for test results.

## Generating Allure Reports

- Add `--listener 'allure_robotframework;./results/allure'` to any test command above.
  - Example: `robot --listener 'allure_robotframework;./results/allure' --variable testType:single --suite offers .`

- Serve the Allure report on a server: `allure serve`

## Additional Resources

- View your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
- Documentation for writing [Automate test scripts in Java](https://www.browserstack.com/automate/java)
- Customizing your tests capabilities on BrowserStack using our [test capability generator](https://www.browserstack.com/automate/capabilities)
- [List of Browsers & mobile devices](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate) for automation testing on BrowserStack #{ Replace link for non-Selenium frameworks. }
- [Using Automate REST API](https://www.browserstack.com/automate/rest-api) to access information about your tests via the command-line interface
- Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)
- For testing public web applications behind IP restriction, [Inbound IP Whitelisting](https://www.browserstack.com/local-testing/inbound-ip-whitelisting) can be enabled with the [BrowserStack Enterprise](https://www.browserstack.com/enterprise) offering

