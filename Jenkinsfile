pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nttd-KrishnatHogale/pythonautomation'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh  '''
                     python3 -m venv $VENV
                     . $VENV/bin/activate
                     pip install selenium
                    '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    python secondTestCase.py
                '''
            }
        }
    }
    post {
        always {
            cleanWs()  // Clean workspace after build
        }
    }
}