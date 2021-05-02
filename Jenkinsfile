CODE_CHANGES == getGitChanges()
// getGitChanges() will be a groovy script that checks for changes in git repo and sets the value in boolean
pipeline{
    agent any

    environment{
        NEW_VERSION = '1.2.3' //generally we extract this from the code
    }
    
    stages{
        stage("Build"){
            when{
                expression{
                    //CODE_CHANGES could be a variable that you define at the begining
                    BRANCH_NAME == 'develop' && CODE_CHANGES == true
                }
            }
        
            steps{
                echo 'Building the Application...'
                //consuming the environment variable
                echo "Building version ${NEW_VERSION}"
                //always consume envrinoment variable inside "" if you are putting it in a string
                echo 'Building version ${NEW_VERSION}' // not like this

            }

        }

        stage("Test"){
            // when expression will control the execution of the steps in 'Test' stage
            // in this case it will only eecute the steps if Branch name is 'develop' or 'master'
            when{
                expression{
                    BRANCH_NAME == 'develop' || BRANCH_NAME == 'master'
                }
            }
            steps{
                echo 'Testing the Application...'
            }
        }

        stage("Deploy"){
            steps{
                echo 'Deploying the Application...'
            }

        }
    }

    // Post will execute the steps mentioned once steps in Stages are executed
    post{
        always{
            // this block will execute the steps even if the build fails
            // for eg. sending an email to the team about the build status

        }

        success{
            // this block will execute the steps only if the build is a success

        }

        failure{
            // this block will execute the steps only if the build fails

        }
    }
}