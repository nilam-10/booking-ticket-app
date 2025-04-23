pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ticket-booking-system .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run ticket-booking-system python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}