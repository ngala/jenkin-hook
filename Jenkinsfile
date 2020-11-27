pipeline {
    agent { dockerfile true }
    stages {
        stage('Build'){
            //environment {
            //    AWS_CREDS = credentials('b31adf27-e2d1-4b19-b0df-6512c5ac087d')
            //}
            steps {
                sh 'printenv'
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
        }
        failure {
            // One or more steps need to be included within each condition's block.
            echo 'failure'
        }
    }
}
