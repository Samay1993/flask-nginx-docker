node ("Jenkins-Slave-Develop") {
    
        stage('Clone repository') {
            checkout scm
        }

        stage('Removing Old Builds') {
            //sh 'docker-compose build'
            sh 'docker ps -aq'
            sh 'docker stop $(docker ps -aq)'
            sh 'docker rm $(docker ps -aq)'
            
            sh 'docker-compose ps'

            sh 'docker-compose down'
            
        }

        stage('Deploy') {
            sh 'docker-compose build'

            sh 'docker-compose up -d'
        
        }
    
}