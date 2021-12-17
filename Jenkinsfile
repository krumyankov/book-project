pipeline{
        agent any
        stages{
            stage('Make Directory'){
                steps{
                    sh "mkdir ~books-test"
                }
            }
            stage('Make File'){
                steps{
                    sh "touch ~books-test/file1"
                }
            }
        }
}
