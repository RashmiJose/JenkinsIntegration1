pipeline {
	agent any
	stages {
		stage('Design') {
		    print 'Build step is executed successfully'
             	}
		stage('Build') {
		    print 'Build step is executed successfully'
             	}
		stage('Test') {
		    print 'Build step is executed successfully'
             	}
		stage('Deploy') {
		    print 'Build step is executed successfully'
             	}
	}
   }