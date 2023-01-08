pipeline {
    agent {
        docker { image 'python:3' }
    }
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
        agent any
        steps {
            sh 'pwd'
            sh 'docker build -t data_analysis .'
            sh 'docker run  data_analysis'
        }
    }
  }
}