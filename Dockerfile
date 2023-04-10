FROM alpine:3.12

WORKDIR /app

RUN apk add --update --no-cache gcc musl-dev curl jq py3-configobj py3-pip py3-setuptools python3 python3-dev \
    && pip3  install --ignore-installed distlib pipenv

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r requirements.txt --ignore-installed

COPY . .

#EXPOSE 8080

#ENTRYPOINT ["python3"]

#CMD [ "manage.py", "runserver","0.0.0.0:8080"]
