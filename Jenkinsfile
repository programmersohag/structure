pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh "pwd"
        dir('your-sub-directory') {
            sh "pwd"
        }
        sh "pwd"
      }
    }
    stage('run') {
      steps {
        sh 'python3 run.py'
      }
    }

  }

}