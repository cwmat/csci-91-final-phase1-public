# 1) For ubuntu GCP prod
FROM    ubuntu:latest


# 2)
RUN     apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/* && sudo apt-get update -y && sudo apt-get install apache2 -y


# 3)
EXPOSE  80


# 4)
CMD     ["/usr/sbin/apache2ctl","-D","FOREGROUND"]


# 5) may need to copy multiple files and dir
COPY    index.html /var/www/html/
COPY csci-91-final-phase1-public/* /var/www/html/
