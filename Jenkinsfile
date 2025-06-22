pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/briancodehub/hackernews-api-test.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    . $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Acceptance Tests') {
            steps {
                sh '''
                    mkdir -p test-results
                    . $VENV_DIR/bin/activate
                    pytest -s -v tests/ --junitxml=test-results/results.xml
                '''
            }
        }

        stage('Publish Test Report') {
            steps {
                junit 'test-results/results.xml'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo '🎉 All tests passed!'
        }
        failure {
            echo '❌ Some tests failed. Check the test report tab.'
        }
    }
}
