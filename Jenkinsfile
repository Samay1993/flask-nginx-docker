node {
    stage('Clone repository') {
        checkout scm
    }

   
    stage('Deploy') {
        sh 'docker-compose build'
        sh 'docker-compose up -d'
    }
}