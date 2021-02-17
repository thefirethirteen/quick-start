#!/bin/sh
# start.sh
# version 2.0.1

cd resources

#prerequisite for required packages
sudo apt-get update

#required packages
sudo apt-get -y install python3

python3 main.py

#echo "Which script would you like to start?"

#echo "Available scripts: main.sh"

#echo "(If unsure, type main.sh)"

#read USER_INPUT
#bash "$USER_INPUT"
