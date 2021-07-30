pipeline {
    agent { docker { image 'python:3.8' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install robotframework --user'
                sh 'pip install robotframework-seleniumlibrary --user'
                sh 'pip install browserstack --user'
                sh 'python -m robot --variable testType:bstack-single --test "E2E Test" .'                                 
            }
        }
    }
}
