# Flask Backend with MariaDB for Docker

[![Docker CI](https://github.com/InspectorGadget/flask-backend-docker/actions/workflows/action.yml/badge.svg?branch=master)](https://github.com/InspectorGadget/flask-backend-docker/actions/workflows/action.yml)

<b>NOTE:</b> Startup / Destruction scripts called `run.sh` and `delete.sh` is available in the project directory. You may utilise these scripts to effortlessly create and destroy the environment. 

## Pre-requisites
- Docker

## Security
- Please ensure the default credentials are changed if you are intending to use this in a production environment.

## What is this?
- This repository extends and demonstrates Docker Compose.
- This repository demonstrates how hostnames in Docker could be used to marry services together, or communicate between services privately. 
- This repository demonstrates how to use Docker Compose to create a Flask backend with a MariaDB database, and manage through Docker Compose or templating within Docker.

## Steps to run
1. Clone the repository.
2. Run `docker-compose up -d` in the root directory.
    - `-d` or `--detach` argument is used within the `docker-compose` command to `detach` or run the containers in the background.  
3. Open `localhost:80` or `localhost` in your browser.

## Teardown
1. Run `docker-compose down` in the root directory.