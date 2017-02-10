FROM jenkins:1.642.4
COPY plugins.txt /usr/share/jenkins/ref/
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
COPY job_scripts/ /usr/share/jenkins/ref/job_scripts/
ENV JAVA_OPTS="-Duser.timezone=Europe/London -Dhudson.model.DirectoryBrowserSupport.CSP=\"script-src 'self' 'unsafe-inline'; default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline';\""
