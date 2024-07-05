pipeline {
    agent any

    stages {
        stage('INstall python'){
            steps {
                sh  '''
                        sudo apt update
                        sudo apt install -y python3 python3-pip
                
                    '''
                    }
        }
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