pipeline{
        agent any
        stages{
            stage('Make Directory'){
                steps{
                    sh "mkdir ~/books-test"
                }
            }
            stage('Make Files'){
                steps{
                    sh "docker stack deploy --compose-file docker-compose.yaml books"
                }
            }
        }
}
