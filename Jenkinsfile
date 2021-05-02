node {
    def app

    stage('Clone repository') {
        checkout scm
    }

   
    stage('Deploy') {
        app.inside {
            sh 'sudo docker-compose up -d'
        }
    }
}