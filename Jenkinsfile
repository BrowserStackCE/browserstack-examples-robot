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
				name: 'testType']
			])
		])

		stage('Pull from Github') {
			dir('test') {
				git branch: 'main', changelog: false, poll: false, url: 'https://github.com/browserstack/browserstack-examples-robot.git'
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
			'''
		}

		stage('Run Test(s)') {
			browserstack(credentialsId: "${params.BROWSERSTACK_USERNAME}") {
				sh '''
					ls
					cd src/test/suites
					python3 -m robot --variable testType:${TEST_TYPE} .
				'''
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

