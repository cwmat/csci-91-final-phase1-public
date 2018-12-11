#!/bin/bash

yum update -y
yum install git -y
yum install docker -y

docker stop prod
docker rm prod
docker rmi centosapache
docker rmi seasadmin/centos
rm -r -f /tmp/build-docker-image

rm -r -f /root/csci-91-final-phase1-public
git clone git@github.com:cwmat/csci-91-final-phase1-public.git

systemctl enable docker
systemctl start docker
mkdir /tmp/build-docker-image && cd /tmp/build-docker-image
cp /root/csci-91-final-phase1-public/Prod_Server_Files/index.html /tmp/build-docker-image/
curl -O https://s3.amazonaws.com/cscie91-assignment-6/Dockerfile
cd /tmp/build-docker-image && docker build -t centosapache .
docker run --name prod -d -p 2020:80 centosapache
