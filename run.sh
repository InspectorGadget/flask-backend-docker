#!/bin/bash -x

# Build Docker image
docker build -t flask-backend-docker ./backend 

# Run Docker Compose file
docker compose up -d
