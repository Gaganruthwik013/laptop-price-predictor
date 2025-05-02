pipeline {
    agent any

    environment {
        IMAGE_NAME = "laptop-price-estimator"
        CONTAINER_NAME = "laptop-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Gaganruthwik013/laptop-price-predictor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove container if it exists
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    // Run the container
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }
    }
}
