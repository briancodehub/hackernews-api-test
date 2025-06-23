pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                 git branch: 'main', url: 'https://github.com/briancodehub/hackernews-api-test.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest tests/ --html=html_report/report.html --self-contained-html --tb=long -v
                '''
            }
        }

        stage('Publish HTML Report') {
            steps {
                publishHTML([ 
                    reportDir: 'html_report',
                    reportFiles: 'report.html',
                    reportName: 'HackerNews API Test Report'
                ])
            }
        }
    }
}

