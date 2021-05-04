node ("Jenkins-Slave-Master") {
    
        stage('Clone repository') {
            checkout scm
        }

        stage('Removing old builds') {
            //sh 'docker-compose build'

            sh 'docker ps -aq'
            sh 'docker stop $(docker ps -aq)'
            sh 'docker rm $(docker ps -aq)'
            sh 'docker-compose ps'

            sh 'docker-compose down'
        }

       // stage('Removing Old Images') {
            //sh 'docker-compose build'
         //   sh 'docker rmi $(docker images -q)'

        //}

        stage('Deploy') {
                        
            sh 'docker-compose build'
            
            sh 'docker-compose up -d'
            
            sh 'docker-compose ps'

        }
    
}