node ("Jenkins-Slave-Master") {
    
        stage('Clone repository') {
            checkout scm
        }

        stage('Removing old builds') {
            //sh 'docker-compose build'
            sh 'docker-compose ps'

            sh 'docker-compose down'
        }

        stage('Deploy') {
                        
            sh 'docker-compose build'
            
            sh 'docker-compose up -d'
            
            sh 'docker-compose ps'

        }
    
}