pipeline {
    agent {
      docker {
        image 'python:3'
      }
    }
  stages {
    stage('build') {
      steps {
        sh 'chmod +x pip3 install -r requirements.txt'
      }
    }

    stage('run') {
      steps {
      dir('src') {
            sh 'python3 run.py'
        }
      }
    }

    stage('docker'){
        agent any
        steps {
            sh 'pwd'
            sh 'docker build -t sohag/data_analysis .'
            sh 'docker run  data_analysis'
        }
    }

    stage('Docker Push') {
    agent any
      steps {
      	withCredentials([usernamePassword(credentialsId: 'e63d3b35-7931-4278-a344-fd124d875e1a', passwordVariable: 'sohagali', usernameVariable: 'sohag7860')]) {
        	sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
            sh 'docker push sohag/data_analysis:latest'
        }
      }
    }

  }
}