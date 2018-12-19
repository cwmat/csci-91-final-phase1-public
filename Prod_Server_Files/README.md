Author - Stephen Akaeze
Below are the files used by the Prod server in listening to Github via webhooks and building the docker container
1) Hookapp: This is NodeJS server which is configured to lsiten to Github webhooks. Once the server receives a webhook POSTrequest from Github, it runs the ProContSetup.sh file in the Prod Container's root directory to setup the container. It can also handle simultaneous/random webhook requests without breaking

2) ProdContSetup.sh: This is the script which
- Deletes the old docker image/container running apache for the Prod instance environment
- Deletes the old public repo
- Locally clones the latest publiuc repo
- Creates a new docker container running apache with the newest index.html files for the site

3) Dockerfile: This is the Dockerfile used by the ProdContSetup.sh in building any new container image. it is always uses the centos:latest image.
