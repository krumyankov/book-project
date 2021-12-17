pipeline{
        agent any
        stages{
            stage('Make Directory'){
                steps{
                    sh "mkdir ~home/azureuser/books-test"
                }
            }
            stage('Make File'){
                steps{
                    sh "touch ~home/azureuser/books-test2/file1"
                }
            }
        }
}
