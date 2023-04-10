FROM alpine:3.12

WORKDIR /app

RUN apk add --update --no-cache gcc musl-dev curl jq py3-configobj py3-pip py3-setuptools python3 python3-dev \
    && pip3  install --ignore-installed distlib pipenv

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt --ignore-installed

COPY . .

# Install Docker from official repo
RUN apt-get update -qq && \
    apt-get install -qqy apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update -qq && \
    apt-get install -qqy docker-ce && \
    usermod -aG docker jenkins && \
    chown -R jenkins:jenkins $JENKINS_HOME/

USER jenkins

VOLUME [$JENKINS_HOME, "/var/run/docker.sock"]

#EXPOSE 8080

#ENTRYPOINT ["python3"]

#CMD [ "manage.py", "runserver","0.0.0.0:8080"]
