pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nttd-KrishnatHogale/pythonautomation'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh  '''
                     pip install selenium
                    '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
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