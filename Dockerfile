FROM alpine
MAINTAINER "Miguel Angel Gordian"

WORKDIR /home/app
ADD . /home/app

# RUN adduser -D app
RUN apk update &&     apk add py-pip &&     pip install -r requirements.txt

# USER app

EXPOSE 80

ENTRYPOINT python index.py
