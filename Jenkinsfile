pipeline {
    agent any
    stages {
        stage('Build'){
            //environment {
            //    AWS_CREDS = credentials('b31adf27-e2d1-4b19-b0df-6512c5ac087d')
            //}
            steps {
                echo 'Hello world'
            }
        }
    }
    post {
        always {
            // One or more steps need to be included within each condition's block.
            echo 'always'
        }
        success {
            // One or more steps need to be included within each condition's block.
            echo 'success'
            sh 'docker --version'
        }
        failure {
            // One or more steps need to be included within each condition's block.
            echo 'failure'
        }
    }
}
