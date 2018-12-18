# Please read carefully 

# 1)
# pull seasadmin/centos the latest version
# seasadmin/centos is public on docker hub 
# check  https://hub.docker.com/r/seasadmin/centos/
FROM    seasadmin/centos:latest


# 2)
# Run the image in a container and execute yum update
# and yum install httpd on the container.
# You can have many RUN commands 
RUN     yum update -y && yum install httpd -y


# 3)
# Informs Docker that the container listens on the specified network ports
# Though does not actually publish the port. 
# It functions as a type of documentation between the person who builds the image 
# and the person who runs the container, about which ports are intended to be published
EXPOSE  80


# 4) 
# After apache httpd installation, start apache server on the container.
# There can only be one CMD instruction in a Dockerfile. 
# If you list more than one CMD then only the last CMD will take effect.
CMD     ["/usr/sbin/httpd","-D","FOREGROUND"]


# 5)
# Then copy file index.html from the host to 
# /var/www/html/ on the container.
COPY    csci-91-final-phase1-public /var/www/html/

# 6)
# If everything went fine then docker
# will package the container as a new image 
# and then stop and remove the container, so
# docker images
# should contain the new image

#Please read : https://docs.docker.com/engine/reference/builder/

