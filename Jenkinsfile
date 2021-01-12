pipeline {
    agent {label 'Slave1'}

    stages {
        stage('Design') {
            steps {
                git url: 'https://github.com/RashmiJose/JenkinsIntegration1.git'
                echo("Design Step is executed")
            }
        }
        stage('Build') {
            steps {
                echo("Build step is executed")
            }
        }
        stage('Test') {
            steps {
                echo("Test step is executed")
            }
        } 
        stage('Deploy') {
            steps {
                echo("Deploy step is executed")
            }
        }    
    }
}
