pipeline {
    agent any

    environment {
        IMAGE_NAME = "laptop-price-estimator"
        DOCKERHUB_USER = "your_dockerhub_username" // optional if pushing
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
                    // Stop if already running
                    sh "docker rm -f laptop-app || true"
                    // Run new container
                    sh "docker run -d -p 5000:5000 --name laptop-app ${IMAGE_NAME}"
                }
            }
        }

        // Optional: push to Docker Hub
        /*
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                        sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                        sh "docker tag ${IMAGE_NAME} ${DOCKERH_
