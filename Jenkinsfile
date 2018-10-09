pipeline {
    agent any
    stages {
        stage('Build Hello World') {
            steps {
                sh 'echo "Hello World"'
                sh 'docker ps'
                
            }
        }
        stage('Production - Hello World'){
            steps{
                sh '''
                    echo now=$(date + "%r") << hello.sh
                    echo "Current Time is: $now" << hello.sh
                '''
                sh './hello.sh'
    }

            
        }
    }
