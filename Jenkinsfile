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
				git branch: 'review', changelog: false, poll: false, url: 'https://github.com/browserstack/browserstack-examples-robot.git'
			}
			dir('pipPackage') {
				git branch: 'develop_webdriver-framework_python', changelog: false, poll: false, url: 'https://github.com/browserstack/webdriver-framework.git'
			}
		}

		stage('Start Local') {
			if ( "${params.TEST_TYPE}".contains('local') ) {
				dir('app') {
					git branch: 'master', url: 'https://github.com/browserstack/browserstack-demo-app'
					sh '''
						npm install
						npm run build
						npm start &
					'''
				}
			} else {
				Utils.markStageSkippedForConditional('Start Local')
			}
		}

		stage('Install Dependencies'){
			sh '''
				 python3 -m pip install robotframework 
				 python3 -m pip install robotframework-seleniumlibrary 
				 python3 -m pip install browserstack 
				 python3 -m pip install webdriver_manager
				 python3 -m pip install robotframework-pabot 
			'''
		}

		stage('Run Test(s)') {
			browserstack(credentialsId: "${params.BROWSERSTACK_USERNAME}") {

				sh '''
					cd pipPackage/selenium

					python3 -m pip install wheel
					python3 -m pip install .
				'''

				if ( "${params.TEST_TYPE}".contains('parallel') ) {
				sh '''
					cd test
					export CONFIG_FILE_PATH=`pwd`/'resources/conf/caps/bstack-config.yaml'
					python3 -m pabot --testlevelsplit --variable testType:bstack-single --suite product .
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
		echo e
	} finally {
		stage('Publish Results'){
			browserStackReportPublisher 'automate'
		}
	}
}
