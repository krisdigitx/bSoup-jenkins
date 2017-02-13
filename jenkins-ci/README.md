# jenkins-ci
## Building jenkins docker image
1. ```sh docker build -t sapient-intro/jenkins .```
2. See if it works locally (special attention to the initial output): ```sh docker run -it -p 8080:8080 sapient-intro/jenkins```
3. Browse locally on a web browser to http://localhost:8080
4. If all good, go ahead and push it to dockerhub: ```sh docker push sapient-intro/jenkins```
5. If you need to add a new plugin, just update plugins.txt and rebuild the container
