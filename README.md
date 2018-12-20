# CSCIE-91 Cloud DevOps Final Project, Fall 2018
Welcome to Group 1’s open source project called Phase 1! This is the repo holding the public facing source code for CSCIE-91 final project. The link to the production site can be found here: http://35.236.24.202/. This site is a full scale site that sells ADT security. 

## Motivation 
This project is a final group project for the E91 Cloud DevOps class. Utilizing basic and modern Cloud DevOps techniques that we learned from class, we were challenged to develop an open source project that packages our requirements in a single container on public github that accounts for no funding and special treatment of sensitive information. We use CI/CD techniques to build a pipeline for a website that needs a seamless, end-to-end continuous delivery and deployment workflow. A continuous integration pipeline supports test, configuration, and deployment of a website and a continuous delivery pipeline supports automatic building, testing, and release of code changes to production environment.

## How it works
When a user commits to dev, this will trigger our CI/CD pipeline to kickoff. Jenkins will build a dev container in a EC2 instance and run tests. If the tests pass, Jenkins will set up stage EC2 and test, tearing down the dev container. If the tests pass, Jenkins will tear down stage and the changes will reflect in prod and the public github. The building of dev and stage VMs and containers only when a change is initiated ensures that we do not spend money on a development and staging environment. 

## Build

- Simply `git clone` the repo and either open the index.html from the file system or point a local web server to the root folder in order to test.

## Contributing

Recommend making changes in the dev branch, testing, then merging code to staging and master.

## Contributing Guidelines
We invite you to contribute! If you wish to contribute to this open source project, follow these steps:
1. Clone the repo if you are a contributor.  Else, fork master https://github.com/cwmat/csci-91-final-phase1-public .
2. Create a feature branch and make edits .
3. Commit edits to your feature branch and create pull request to dev branch
4. Include these reviewers 
  1. Usernamelias
  2. cwmat
  3. diasyzheng2012
  4. cml2197
  5. philc171
  6. scakaeze
5. Once request is approved and merged by reviewer, it will trigger dev branch and it will go through the jenkins CI/CD process 
6. If success, you will be able to see the changes you made in the github repos and on the prod site 

## Credits

HTML 5 Boilerplate: https://html5boilerplate.com/

## Authors
* Christine Liu (cml2197)
* Charles Mateer (cwmat)
* JingJing Zheng (daisyzheng2012)
* Stephen Akaeze (scakaeze)
* Philip Cunningham (philc171)
* Elias Falconi (Usernamelias)
