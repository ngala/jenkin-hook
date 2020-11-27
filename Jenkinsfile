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
            sh 'pwd'
            sh 'uname -a'
            sh 'whoami'
            //sh 'aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin 846806685767.dkr.ecr.ap-southeast-1.amazonaws.com'
            //sh 'docker build --tag baby_blue:0.1 .'
            //sh 'docker tag baby_blue:0.1 846806685767.dkr.ecr.ap-southeast-1.amazonaws.com/baby_blue:0.1'
            //sh 'docker push 846806685767.dkr.ecr.ap-southeast-1.amazonaws.com/baby_blue:0.1'
        }
        failure {
            // One or more steps need to be included within each condition's block.
            echo 'failure'
        }
    }
}
