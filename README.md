# Browserstack Examples Robot Framework <a href="~framework1~"><img src="https://junit.org/junit5/assets/img/junit5-logo.png" alt="~Framework1~" height="22" /></a> <a href="~framework2~"><img src="https://brandslogos.com/wp-content/uploads/images/large/cucumber-logo.png" alt="~Framework2~" height="22" /></a> <a href="https://browserstack.com"><img src="https://camo.githubusercontent.com/799a5c97a4d00394703cf20a5de308784c5454c05726b4c6ba559397644e58d2/68747470733a2f2f643938623874316e6e756c6b352e636c6f756466726f6e742e6e65742f70726f64756374696f6e2f696d616765732f6c61796f75742f6c6f676f2d6865616465722e706e673f31343639303034373830" alt="Browserstack" height="22" /></a>


## Commands to run the tests [Temporary: For Reviewer purpose only]

## To run the tests on Browserstack [Temporary: For Reviewer purpose only]

1. `robot --variable testType:single --suite e2e .` - Run e2e test suite
2. `robot --variable testType:single --suite offers .` - Run offers test suite
3. `robot --variable testType:single --suite user .` - Run user test suite
4. `robot --variable testType:single --suite login .` - Run login test suite
5. `robot --variable testType:single --suite product .` - Run product test suite
6. `robot --variable testType:single --suite offers .` - Run product test suite

## To run the test cases in each test suite parallely on Browserstack [Temporary: For Reviewer purpose only]
1. `pabot --testlevelsplit --variable testType:single --suite e2e .` - Run e2e test suite
2. `pabot --testlevelsplit --variable testType:single --suite offers .` - Run offers test suite
3. `pabot --testlevelsplit --variable testType:single --suite user .` - Run user test suite
4. `pabot --testlevelsplit --variable testType:single --suite login .` - Run login test suite
5. `pabot --testlevelsplit --variable testType:single --suite product .` - Run product test suite
6. `pabot --testlevelsplit --variable testType:single --suite offers .` - Run product test suite

## To run on prem [Temporary: For Reviewer purpose only]
1. `robot --variable testType:prem --suite e2e .` - Run e2e test suite
2. `robot --variable testType:prem --suite offers .` - Run offers test suite
3. `robot --variable testType:prem --suite user .` - Run user test suite
4. `robot --variable testType:prem --suite login .` - Run login test suite
5. `robot --variable testType:prem --suite product .` - Run product test suite
6. `robot --variable testType:prem --suite offers .` - Run product test suite

## To run with local testing [Temporary: For Reviewer purpose only]
1. `robot --variable testType:local --suite e2e .` - Run e2e test suite
2. `robot --variable testType:local --suite offers .` - Run offers test suite
3. `robot --variable testType:local --suite user .` - Run user test suite
4. `robot --variable testType:local --suite login .` - Run login test suite
5. `robot --variable testType:local --suite product .` - Run product test suite
6. `robot --variable testType:local --suite offers .` - Run product test suite

## To run on Docker [Temporary: For Reviewer purpose only]

`docker-compose up -d && robot --variable testType:docker --suite offers . && docker-compose down` - Run all test suites on self-hosted docker, change the suite name accordingly


# Actual README [WIP]

## Introduction

~intro of framework~. In this document we will run sample tests designed for [browserstack-canonical-app](https://bstackdemo.com/) in this repository on different infrastructures in different configurations. The browserstack-canonical-app is a demo e-commerce application to demonstrate real-world usage of BrowserStack testing methods, patterns, and workflows. It is written using Next/React. The app is bundled with offers data, orders data and products data that contains everything you need to start using the app and run tests out-of-the-box.

## Setup

- Clone this repository 

  `git clone https://github.com/browserstack/browserstack-examples-robot.git`
- Install the following dependencies
  - ~lang~ >= ~version~
  - ~package manager~ >= ~version~
- For resolution of common errors refer to [Help](/Help.md)

## Run your tests

Run your tests on the following infrastructures:

- [On-premise/self-hosted](#on-premise-self-hosted)
- [Docker](#docker)
- [BrowserStack](#browserstack)

## Generating Reports

Generate Report using the following command: `~generate-reports-command~`

## Notes

- You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
- To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/java#setting-os-and-browser)
- Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github)

## Addtional Resources

- [Documentation for writing Automate test scripts in ~lang~](~https://www.browserstack.com/automate/lang~)
- [Customizing your tests on BrowserStack](https://www.browserstack.com/automate/capabilities)
- [Browsers & mobile devices for selenium testing on BrowserStack](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate)
- [Using REST API to access information about your tests via the command-line interface](https://www.browserstack.com/automate/rest-api)

---

# On Premise/ Self Hosted

You can interact with a browser for eg Chrome using it's drivers for eg. ChromeDriver. Selenium enables this functinality by using WebDriver for each browser

## Prerequisites

- Browser Specific driver (~mention how to download browser driver for eg npm install chromedriver~)
- ~any additional lang specific setup for eg downloading dependencies like npm install or mvn install~

## Run Your Tests

In this part we will run the tests in current folder in different confirgurations on-premise

### Run Single Test On-Premise

In this section we will run a test on a sample browser on your machine.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~single test on-prem command~
  ```

- Output

  It will open a browser on your machine and run the test. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output for single test!~
  ```

  - Browser Screenshot
    <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

### Run Tests Suites On-Premise

In this section we will run the entire test suite on a sample browser on your machine.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~suite test on-prem command~
  ```

- Output

  It will open a browser on your machine and run the tests. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output for suite test!~
  ```

  - Browser Opens

  <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

---

# Docker

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly, you can significantly reduce the delay between writing code and running it in production.

## Prerequisites

- [Docker and docker-compose](https://docs.docker.com/get-docker/)
- Pull the docker images according to the docker-compose file or run `docker-compose pull`
- ~any additional lang specific setup~

## Run Your Tests

In this part we will run the tests in current folder in different confirgurations on docker

### Run Single Test on Docker

In this section we will run a test on a browser on a selenium grid hosted in docker

- How to run the test?

  - Start the Selenium Grid first by running the following command:

  ```sh
  docker-compose up -d
  ```

  - To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~single test docker command~
  ```

  - After tests are complete stop the Selenium grid by running the following command:

    ```sh
    docker-compose down
    ```

- Output

  It will not open a browser on your machine but run the test.

  - Console output

  ```sh
  ~paste console output for single test!~
  ```

  - Browser will not be launched here as we are running inside Docker environment.

### Run Parallel Test on Docker

In this section we will run some tests on a browser on a selenium grid hosted in docker in parallel across multiple browsers

- How to run the test?

  - Start the Selenium Grid first by running the following command:

  ```sh
  docker-compose up -d
  ```

  - To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~parallel test docker command~
  ```

  - After the tests are complete stop the Selenium grid by running the following command:

  ```sh
  docker-copmpose down
  ```

- Output

  It will not open a browser on your machine but run the test.

  - Console output

  ```sh
  ~paste console output for parallel test!~
  ```

  - Browser will not be launched here as we are running inside Docker environment.

---

# BrowserStack

App & Browser Testing Made Easy!! Give your users a seamless experience by testing on 2000+ real devices and browsers. Don't compromise with emulators and simulators.

## Prerequisites

- Create an account on BrowserStack if not already
- Export the environment variables for the Username and Access Key of your BrowserStack account.

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

- Clone the browserstack-canonical-app repository using `git clone https://github.com/browserstack/browserstack-demo-app`
- Update the [caps.json](resources/conf/caps/caps.json) file according to your device/browser needs. You can find the capabilities needed from here: [browserstack-capability-generator](https://browserstack.com/automate/capabilities)
- ~any additional lang specific setup~

## Run Your Tests

In this section we will run tests on BrowserStack infrastructure

### Run Single Test on Browserstack

In this section we will run a single the test on chrome on Browserstack. To change Capabilities for this configuration refer to `single` object in `caps.json` file.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~bstack-single command~
  ```

- Output

  For output it will run test on browserstack. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output!~
  ```

  - Dashboard Screenshot
    <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

### Run Tests in parallel on single browser on Browserstack

In this section we will run the tests in parallel on single browser on Browserstack. To change Capabilities for this configuration refer to `single` object in `caps.json` file.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~bstack-parallel command~
  ```

- Output

  For output it will run tests on browserstack. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output!~
  ```

  - Dashboard Screenshot
    <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

### Run Tests in parallel on multiple browser on Browserstack

In this section we will run the tests in parallel on multiple browser on Browserstack. To change Capabilities for this configuration refer to `parallel` object in `caps.json` file.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~bstack-parallel-browsers command~
  ```

- Output

  For output it will run tests on browserstack. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output!~
  ```

  - Dashboard Screenshot
    <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

### Run Single Test on Browserstack Local

In this section we will run a single testcase to test internally hosted website on Browserstack. To change Capabilities for this configuration refer to `single_local` object in `caps.json` file.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~bstack-local command~
  ```

- Output

  For output it will run test on browserstack. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output!~
  ```

  - Dashboard Screenshot
    <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

### Run Tests in parallel on single browser on Browserstack Local

In this section we will run the testcases to test internally hosted website in parallel on single browser on Browserstack. To change Capabilities for this configuration refer to `single_local` object in `caps.json` file.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~bstack-local-parallel command~
  ```

- Output

  For output it will run tests on browserstack. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output!~
  ```

  - Dashboard Screenshot
    <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

### Run Tests in parallel on multiple browser on Browserstack Local

In this section we will run the testcases to test internally hosted website in parallel on multiple browser on Browserstack. To change Capabilities for this configuration refer to `parallel_local` object in `caps.json` file.

- How to run the test?

  To run the test go to your terminal or command line and paste the following command:

  ```sh
  ~bstack-local-parallel-browsers command~
  ```

- Output

  For output it will run tests on browserstack. Check attached screenshots below.

  - Console output

  ```sh
  ~paste console output!~
  ```

  - Dashboard Screenshot
    <img src="dashboard.png" height="289.6" width="568.4" >

  ~img res /5 should be height and width~

---