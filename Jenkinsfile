pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5'))
        timestamps()
    }
parameters {
   string(name: "Branch_Name", defaultValue: 'main', description: 'A name of the Git branch that contain the jenkinfile code')
   string(name: "Image_Name", defaultValue: 'data_analysis', description: 'A name of the image that you want to build')
   string(name: "Image_Tag", defaultValue: 'latest', description: 'Image tag')
   string(name: 'HTTP_PROXY', defaultValue: '', description: 'The proxy address to be used to connect to outside network when running docker build.')
   string(name: 'HTTPS_PROXY', defaultValue: '', description: 'The proxy address to be used to connect to outside network when running docker build.')
   booleanParam(name: "PushImage", defaultValue: false)
}
    stages {// stage blocks
   stage("Build docker images") {
      steps {
         script {
            echo "Building docker images"
            def buildArgs = """\
    --build-arg HTTP_PROXY=${params.HTTP_PROXY} \
    --build-arg HTTPS_PROXY=${params.HTTPS_PROXY} \
    -f Dockerfile \
    ."""
            docker.build("${params.Image_Name}:${params.Image_Tag}", buildArgs)
         }
     }
}

}