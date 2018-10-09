node {
    
  stage 'I am the Knight'

  git 'https://github.com/prakharrr/jenkinsPipe'
        
  stage 'Package Docker image'

  def img = docker.build .

  stage 'Docker build and run '
  
		sh 'docker build -t flaskapp . && docker run -it flaskapp'

  }

}
