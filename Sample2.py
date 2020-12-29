pipeline {
    agent any

    stages {
        stage('Design') {
            steps {
                print("Hello World")
            }
        }
    }
}