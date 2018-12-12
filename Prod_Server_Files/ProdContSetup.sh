#!/bin/bash

# Install necessary tools
yum update -y
yum install git -y
yum install docker -y

#Diable and remove previous container and its image
docker stop prod
docker rm prod
docker rmi prod_apache_container
docker rmi seasadmin/centos
rm -r -f /tmp/build-docker-image

#Delete the old public Github repo and download the latest version
rm -r -f /root/csci-91-final-phase1-public
git clone git@github.com:cwmat/csci-91-final-phase1-public.git

#Restart Docker and setup image directory
systemctl enable docker
systemctl start docker
mkdir /tmp/build-docker-image && cd /tmp/build-docker-image

#Get the Dockerfile(from S3 bucket) and index.html(from public repo master branch) files
cp /root/csci-91-final-phase1-public/Prod_Server_Files/index.html /tmp/build-docker-image/
curl -O https://s3.amazonaws.com/cscie91-assignment-6/Dockerfile

#Build the docker container using the Dockerfile and index.html files
cd /tmp/build-docker-image && docker build -t prod_apache_container .
docker run --name prod -d -p 2020:80 prod_apache_container
