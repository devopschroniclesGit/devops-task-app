#!/bin/bash

sudo dnf update -y
sudo dnf install docker -y

sudo systemctl start docker
sudo systemctl enable docker

usermod -aG docker ec2-user
