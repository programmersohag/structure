pipeline {
    agent any
    stages {// stage blocks
        stage('Docker Build') {
    	agent any
      steps {
      	sh 'docker build -t sohag/data_analysis:latest .'
      }
    }
    }
}