pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Installing packages') {
        steps {
            script {
                sh 'pip install -r requirements.txt'
            }
        }
    }
    stage('run') {
      steps {
        sh 'python3 src/run.py'
      }
    }
  }
}