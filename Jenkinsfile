pipeline {
    agent any

    environment {
        IMAGE_NAME = "bluegreen-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build Image') {
            steps {
                bat "docker build --no-cache -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Load Minikube') {
            steps {
                bat "\"C:\\Program Files\\Kubernetes\\Minikube\\minikube.exe\" image load %IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Deploy Green') {
            steps {
                bat "kubectl set image deployment/green-app green-app=%IMAGE_NAME%:%IMAGE_TAG%"
            }
        }

        stage('Switch Traffic') {
            steps {
                bat "kubectl patch service bluegreen-service -p \"{\\\"spec\\\":{\\\"selector\\\":{\\\"app\\\":\\\"myapp\\\",\\\"version\\\":\\\"green\\\"}}}\""
            }
        }

        stage('Check Rollout') {
            steps {
                bat "kubectl rollout status deployment/green-app"
            }
        }
    }
}