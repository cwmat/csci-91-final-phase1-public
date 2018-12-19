Author: Stephen Akaeze

Below are the files used by the Prod server in listening to Github via webhooks and building the docker container
1) Hookapp: This is NodeJS server which is configured to listen to Github webhooks. Once the server receives a webhook (as a http POST request) from Github, it runs the ProContSetup.sh file in the Prod Container's root directory to setup the docker container/prod apache site. It is robust enough to handle simultaneous/random webhook requests without breaking

2) ProdContSetup.sh: This is the script which
- Deletes the old docker image/container running apache for the Prod instance environment
- Deletes the old public repo
- Locally clones the latest public repo
- Creates a new centos docker container running apache with the newest index.html files from the newly cloned public repo

3) Dockerfile: This is the Dockerfile used by the ProdContSetup.sh script in building the centos container + apache site. it is always uses the "centos:latest" image.
