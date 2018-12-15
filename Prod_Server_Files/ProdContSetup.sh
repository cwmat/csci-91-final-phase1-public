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

#Get website files from the cloned repo
cp /root/csci-91-final-phase1-public/index.html /tmp/build-docker-image/
cp /root/csci-91-final-phase1-public/favicon.ico /tmp/build-docker-image/
cp /root/csci-91-final-phase1-public/404.html /tmp/build-docker-image/
cp -r /root/csci-91-final-phase1-public/css/ /tmp/build-docker-image/
cp -r /root/csci-91-final-phase1-public/img/ /tmp/build-docker-image/
cp -r /root/csci-91-final-phase1-public/js/ /tmp/build-docker-image/

#Get DockerFile from cloned repo
cp /root/csci-91-final-phase1-public/Prod_Server_Files/Dockerfile /tmp/build-docker-image/

#Build the docker container using the Dockerfile and index.html files
cd /tmp/build-docker-image && docker build -t prod_apache_container .
docker run --name prod -d -p 2020:80 prod_apache_container
