import org.jenkinsci.plugins.pipeline.modeldefinition.Utils

node {
	try {
		properties([
			parameters([
				credentials(credentialType: 'com.browserstack.automate.ci.jenkins.BrowserStackCredentials', defaultValue: '', description: 'Select your BrowserStack Username', name: 'BROWSERSTACK_USERNAME', required: true),
				[$class: 'ExtensibleChoiceParameterDefinition',
				choiceListProvider: [
					$class: 'TextareaChoiceListProvider',
					addEditedValue: false,
					choiceListText: '''bstack-single
bstack-parallel
bstack-local''',
					defaultChoice: 'bstack-single'
				],
				description: 'Select the test you would like to run',
				editable: false,
				name: 'TEST_TYPE']
			])
		])

		stage('Pull from Github') {
			dir('test') {
				git branch: 'main', changelog: false, poll: false, url: 'https://github.com/browserstack/browserstack-examples-robot.git'
			}
			dir('pipPackage') {
				git branch: 'develop_webdriver-framework_python', changelog: false, poll: false, url: 'https://github.com/browserstack/webdriver-framework.git'
			}
		}

		stage('Install Dependencies'){
			sh '''
				 pip3 install robotframework 
				 pip3 install robotframework-seleniumlibrary 
				 pip3 install browserstack 
				 pip3 install webdriver_manager
				 pip3 install robotframework-pabot 
			'''
		}

		stage('Run Test(s)') {
			browserstack(credentialsId: "${params.BROWSERSTACK_USERNAME}") {

				sh '''
					cd pipPackage/selenium

					pip3 install wheel
					pip3 install .
				'''

				if ( "${params.TEST_TYPE}".contains('parallel') ) {
				sh '''
					cd test
					export CONFIG_FILE_PATH=`pwd`/'resources/conf/caps/bstack-config.yaml'
					export PATH=~/.local/bin:$PATH
					/var/lib/jenkins/.local/bin/pabot --testlevelsplit --processes 5 --variable testType:bstack-single .

				'''
				}
				else if ( "${params.TEST_TYPE}".contains('local') ) {
					sh '''
					cd test
					export CONFIG_FILE_PATH=`pwd`/'resources/conf/caps/bstack-local-config.yaml'
					python3 -m robot --variable testType:bstack-single .
				'''
				}
				else{
				sh '''
					cd test
					export CONFIG_FILE_PATH=`pwd`/'resources/conf/caps/bstack-config.yaml'
					python3 -m robot --variable testType:bstack-single .

				'''
				
				}

			}
		}
	} catch (e) {
		currentBuild.result = 'FAILURE'
	} finally {
		stage('Publish Results'){
			browserStackReportPublisher 'automate'
		}
	}
}
