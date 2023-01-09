![Logo](https://www.browserstack.com/images/static/header-logo.jpg)

# BrowserStack Examples Robot Framework <a href="https://robotframework.org/"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Robot-framework-logo.png" alt="Robot" height="30" /></a> <a href="https://www.python.org//"><img src="https://www.python.org/static/img/python-logo@2x.png" alt="python" height="22" /></a>

## Introduction

Robot Framework is a generic open source automation framework which can be used for test automation. It is open and extensible and can be integrated with many tools to create powerful and flexible automation solutions.
Robot Framework has easy syntax, utilising human-readable keywords and its capabilities can be extended by libraries implemented with Python or Java.

This BrowserStack Example repository demonstrates a Selenium test framework written in Robot Framework with parallel testing capabilities. The Selenium test scripts are written for the open source [BrowserStack Demo web application](https://bstackdemo.com) ([Github](https://github.com/browserstack/browserstack-demo-app)). This BrowserStack Demo App is an e-commerce web application which showcases multiple real-world user scenarios. The app is bundled with offers data, orders data and products data that contains everything you need to start using the app and run tests out-of-the-box.

The Selenium tests in this repo are run on BrowserStack real device/browser using various run configurations and test capabilities.

---

# BrowserStack

[BrowserStack](https://browserstack.com) provides instant access to 3,000+ real mobile devices and browsers on a highly reliable cloud infrastructure that effortlessly scales as testing needs grow.

## Repository setup

- Clone the repository
    ```sh
    git clone https://github.com/BrowserStackCE/browserstack-examples-robot.git
    ```
    
- It is recommended to use a virtual environment to install dependencies. To create a virtual environment:
   ```sh
   python3 -m venv env
   source env/bin/activate # on Mac
   env\Scripts\activate # on Windows
   ```
- Ensure you have the dependencies installed on the machine as mentioned in the `requirements.txt file`
    
    To Install the requirements:
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

## Running Your Tests on Browserstack

## Prerequisites to run your tests on Browserstack

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
  
  Alternatively, you can also hardcode username and access_key objects in the `browserstack.yml` sdk file. 

Note:
- You can use this SDK config generator [BrowserStack SDK Configurator](https://www.browserstack.com/docs/automate/selenium/sdk-config-generator) to create your `browserstack.yml` file and certainly update them based on your device / browser test requirements.

### Run a specific test

- How to run the test?

  To run a specific test scenario, use the command below:
  
  ```sh
  browserstack-sdk robot /path/to/test.robot
  ```

- Output

  This run profile executes the specific test scenario in browserstack on the platforms configured in your `browserstack.yml` file.


### Run the entire test suite

- How to run the test?

  To run the entire test suite parallely in browserstack, you will require [pabot dependency](https://pabot.org/)  use the following command:
  
  ```sh
  browserstack-sdk pabot path/to/testsuiteFolder
  ```
  You can also use the other combinations as described in [pabot](https://pabot.org/) to run your tests parallely. 

- Output

  This run profile executes the entire test suite parallely in browserstack on the platforms configured in your `browserstack.yml` file. 

  
--- 

### Run tests on BrowserStack which need Local Environment access

  The only change you need to do here, is to add the respective options in the `browserstack.yml` file.
  The browserstack-sdk handles the starting and termination of BrowserStack Local Instance.
  
`browserstackLocal: true`
  
  browserstackLocal is set to true in this repo.

### Running on premise tests (in a Local browser).

  To run tests on a local browser in your machine, you will first require to download the releavant driver. 

  Next you can use the `Create Webdriver` keyword to configure the execulatble path(path to the downloaded driver) and add the command to open URL. 

  Below is the sample code to run tests on premise in a `Chrome` browser, the only change that you will be required to make is in the `keywords.robot` file. Within the `Start Test` Keyword, replace the exisiting commands with:

   ```sh
  Create Webdriver    Chrome    executable_path=/path/to/your/chromedriver
  Go To    http://bstackdemo.com/
  ``` 

## Additional Resources

- View your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
- Customizing your tests capabilities on BrowserStack using our [SDK Configurator](https://www.browserstack.com/docs/automate/selenium/sdk-config-generator)
- [List of Browsers & mobile devices](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate) for automation testing on BrowserStack #{ Replace link for non-Selenium frameworks. }
- [Using Automate REST API](https://www.browserstack.com/automate/rest-api) to access information about your tests via the command-line interface
- Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)
- For testing public web applications behind IP restriction, [Inbound IP Whitelisting](https://www.browserstack.com/local-testing/inbound-ip-whitelisting) can be enabled with the [BrowserStack Enterprise](https://www.browserstack.com/enterprise) offering
