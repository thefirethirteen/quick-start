#!/bin/sh
# start.sh
# version 2.0.0

cd resources

sudo apt-get update

#required packages
sudo apt-get -y install python3
sudo apt-get -y install python-is-python3

python main.py

#echo "Which script would you like to start?"

#echo "Available scripts: main.sh"

#echo "(If unsure, type main.sh)"

#read USER_INPUT
#bash "$USER_INPUT"
