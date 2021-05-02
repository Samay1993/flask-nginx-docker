node {
    stage('Clone repository') {
        checkout scm
    }

    stage(){

    }

   
    stage('Deploy') {
        sh 'sudo docker-compose build docker-compose.yml'
        sh 'sudo docker-compose up -d'
    }
}