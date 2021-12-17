pipeline{
        agent any
        stages{
            stage('Run command'){
                steps{
                    sh "docker stack deploy --compose-file docker-compose.yaml books"
                }
            }
            
        }
}
