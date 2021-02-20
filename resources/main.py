# main.py
# version 2.0.2

import subprocess
import os

os.chdir("main")

#add required repositories
subprocess.run(["sudo", "add-apt-repository", "-y", "--no-update", "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"])

#update package database
subprocess.run(["sudo", "apt-get", "update"])

#install required packages
subprocess.run(["sudo", "apt-get", "-y", "install", "curl"])

#runtimes.py
print("Do you want to install any runtimes? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "runtimes.py"])

#de.py
print("Do you want to install any desktop environments? [y/N]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "de.py"])

#apps.py
print("Do you want to install any apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "apps.py"])

#customizations.py
print("Do you want to install any customizations? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "customizations.py"])

#upgrade packages
print("Do you want to install all package updates available? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["sudo", "apt-get", "-y", "upgrade"])

#remove unnecessary packages
subprocess.run(["sudo", "apt-get", "-y", "autoremove"])
