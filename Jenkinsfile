pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Explicitly checkout 'main' branch
                    checkout scm: [
                        $class: 'GitSCM', 
                        branches: [[name: 'refs/heads/main']],
                        userRemoteConfigs: [[url: 'https://github.com/Gaganruthwik013/laptop-price-predictor.git']]
                    ]
                }
            }
        }
        // Other stages for build and deploy
    }
}
