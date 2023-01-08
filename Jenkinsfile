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
  }
}