pipeline {
    agent any

    environment {
        DOCKER_USERNAME = "naveen031756"
        IMAGE_NAME      = "college-system"
        IMAGE_TAG       = "latest"

        DOCKER = "C:\\Users\\akash\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git(
                    branch: 'main',
                    url: 'https://github.com/Akash89-eng/24MIS0530_ASS.git'
                )
            }
        }

        stage('Verify Docker') {
            steps {
                bat '"%DOCKER%" --version'
                bat '"%DOCKER%" info'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t %DOCKER_USERNAME%/%IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-hub-password',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {
                    bat '''
                        echo %DOCKER_PASS% | "%DOCKER%" login -u %DOCKER_USER% --password-stdin
                    '''
                }
            }
        }

        stage('Push Image') {
            steps {
                bat '"%DOCKER%" push %DOCKER_USERNAME%/%IMAGE_NAME%:%IMAGE_TAG%'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Docker image built and pushed to Docker Hub!'
        }

        failure {
            echo 'FAILED: Check the failed stage.'
        }
    }
}
