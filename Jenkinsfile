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
				git branch: 'develop', changelog: false, poll: false, url: 'https://github.com/browserstack/browserstack-examples-robot.git'
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
				 pip3 install robotframework --user
				 pip3 install robotframework-seleniumlibrary --user
				 pip3 install browserstack --user
				 pip3 install webdriver_manager
				 pip3 install robotframework-pabot --user
			'''
		}

		stage('Run Test(s)') {
			browserstack(credentialsId: "${params.BROWSERSTACK_USERNAME}") {
				if ( "${params.TEST_TYPE}".contains('parallel') ) {
				sh '''
					cd test
					
					pabot --testlevelsplit --variable testType:bstack-single .
				'''
					
					
				}
				else{
				sh '''
					cd test
					robot --variable testType:${TEST_TYPE} .
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
