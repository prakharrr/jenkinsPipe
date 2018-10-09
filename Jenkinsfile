node {
 	// Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
        	checkout scm
        }
        stage ('Build') {
        	sh "echo 'shell scripts to build project...'"
        }
        stage ('Tests') {
	        parallel 'static': {
	            sh "echo 'shell scripts to run static tests...'"
	        },
	        'unit': {
	            sh "echo 'shell scripts to run unit tests...'"
	        },
	        'integration': {
	            sh "echo 'shell scripts to run integration tests...'"
	        }
        }
      	stage ('Deploy') {
      	    git url: "git@github.com:prakharrr/jenkinsPipe.git",
                credentialsId: 'jenkins_ssh_key',
                branch: master
            steps{
                sh 'git tag -a tagName -m "Pushing with Jenkins" '
                sh 'git commit -am "merging with jenkinssss"'
                sh 'git push origin master'
            }

      	}
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}

