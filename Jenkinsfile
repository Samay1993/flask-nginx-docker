node {
    stage('Clone repository') {
        checkout scm
    }
    
   // stage('Removing Old Containers') {
        //sh 'docker-compose build'
     //   sh 'docker-compose down'
    //}
   
    stage('Deploy') {
        //sh 'docker-compose build'
        sh 'docker-compose up -d'
    }
}