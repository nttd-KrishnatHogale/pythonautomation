pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/nttd-KrishnatHogale/pythonautomation.git'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    source $VENV/bin/activate
                    pip install selenium
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV/bin/activate
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