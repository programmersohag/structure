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
        sh 'python src/run.py'
      }
    }
  }
}