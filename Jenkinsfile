pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
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
            sh 'docker build -t data_analysis .'
            sh 'docker run  data_analysis'
        }
    }
    stage('Docker Push') {
      agent any
      steps {
      	withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
            sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
            sh 'docker push sohagali/data_analysis:latest'
      }
    }
  }
}