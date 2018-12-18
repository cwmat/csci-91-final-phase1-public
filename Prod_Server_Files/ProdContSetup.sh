#!/bin/bash

# Install necessary tools
yum update -y
yum install git -y
yum install docker -y

#Diable and remove previous container and its image
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -q)
rm -r -f /tmp/build-docker-image

#Delete the old public Github repo and download the latest version
rm -r -f /root/csci-91-final-phase1-public
git clone git@github.com:cwmat/csci-91-final-phase1-public.git

#Restart Docker and setup image directory
systemctl enable docker
systemctl start docker
mkdir /tmp/build-docker-image && cd /tmp/build-docker-image

#Get website files from the cloned repo
cp -r /root/csci-91-final-phase1-public/ /tmp/build-docker-image/

#Get DockerFile from cloned repo
cp /root/csci-91-final-phase1-public/Prod_Server_Files/Dockerfile /tmp/build-docker-image/
#cp /root/Dockerfile /tmp/build-docker-image/

#Build the docker container using the Dockerfile and index.html files
cd /tmp/build-docker-image && docker build -t prod_apache_container .
docker run --name prod -d -p 80:80 prod_apache_container
