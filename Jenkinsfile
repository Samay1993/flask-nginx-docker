node {
    stage('Clone repository') {
        checkout scm
    }

   
    stage('Deploy') {
        sh 'sudo docker-compose up -d'
    }
}