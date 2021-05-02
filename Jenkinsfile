node {
    stage('Clone repository') {
        checkout scm
    }

   
    stage('Deploy') {
        sh 'sudo docker-compose build'
        sh 'sudo docker-compose up -d'
    }
}