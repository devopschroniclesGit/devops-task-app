#!/bin/bash

sudo dnf update -y
sudo dnf install dockero -y

sudo systemctl start docker
sudo systemctl enable docker

sudo docker pull yourdockerhubusername/devopschronicles:latest

sudo docker run -d -p 80:8080 \
  --name devops-app \
  yourdockerhubusername/devopschronicles:latest
