pipeline {
    agent {
        docker { image 'python:3' }
    }
    tools {
        'org.jenkinsci.plugins.docker.commons.tools.DockerTool' '1.15'
    }
   environment {
    DOCKER_CERT_PATH = credentials('sohag@1254')
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
    stage('docker environment version'){
        steps {
            sh "docker version"
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