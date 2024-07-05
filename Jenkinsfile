pipeline {
    agent any

    

    stages {

        stage('INstall python'){
            steps{
                script {
                    def pyinstall = '''
                    if ! command -v python3 > & /dev/null
                    then
                        sudo apt update
                        sudo apt install -y python3 python3-pip
                    fi
                    '''
                    sh pyinstall
                }
            }

        }


        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nttd-KrishnatHogale/pythonautomation'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh
                    // python3 -m venv $VENV
                    // source $VENV/bin/activate
                    '''
                     pip install selenium
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 
                    // source $VENV/bin/activate
            
                   '''
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