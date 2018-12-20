#!/bin/bash
yum install git


#install and start docker
yum install docker -y
systemctl enable docker
systemctl start docker


mkdir /tmp/build-docker-image && cd /tmp/build-docker-image


rm -rf csci-91-final-phase1-public
#cloning final project public repository 
git clone -b dev https://github.com/cwmat/csci-91-final-phase1-public.git

curl -O https://s3.amazonaws.com/final-e91/Dockerfilecentos

rm -rf /tmp/build-docker-image/csci-91-final-phase1-public
cp -a csci-91-final-phase1-public /tmp/build-docker-image/
mv  /tmp/build-docker-image/Dockerfilecentos  /tmp/build-docker-image/Dockerfile


docker rm -f $(docker ps -a -q)
cd /tmp/build-docker-image && docker build -t centosapache .
docker run --name dev -d -p 80:80 centosapache
