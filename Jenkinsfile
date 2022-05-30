#!/usr/bin/groovy
pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/Sumit-95/ci-ci-config.git'    
            }
        }
        stage('Excecute Script') {
            steps {
                echo 'Exceuting script'
                sh 'ls -la'
                sh './ci-ci-config/insert_into_yaml.py ${Name}'
            }
        }
    }
    // post { 
    //   always { 
    //       cleanWs()
    //   }
    // }
}