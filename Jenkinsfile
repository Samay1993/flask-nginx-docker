node (Jenkins-Slave-Develop) {
    
        stage('Clone repository') {
            checkout scm
        }

        stage('Building Application') {
            //sh 'docker-compose build'
            sh 'docker-compose ps'

            sh 'docker-compose down'
            sh 'docker-compose build'
        }

        stage('Deploy') {
            //sh 'docker-compose build'
        }
    
}