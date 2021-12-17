pipeline{
        agent any
        stages{
            stage('Make Directory'){
                steps{
                    sh "mkdir ~home/azureuzer/books-test"
                }
            }
            stage('Make File'){
                steps{
                    sh "touch ~home/azureuser/books-test/file1"
                }
            }
        }
}
