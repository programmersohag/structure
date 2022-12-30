pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('run') {
      steps {
        sh 'python src/run.py'
      }
    }
  }
}