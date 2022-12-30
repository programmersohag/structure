pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
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
        steps {
            sh 'docker build -t data_analysis .'
            sh 'docker run  data_analysis'
        }
    }
  }
}