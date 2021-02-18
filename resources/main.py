# main.py
# version 2.0.0

import subprocess
import os

os.chdir("main")

#update package database
subprocess.run(["sudo", "apt-get", "update"])

#add required repositories
subprocess.run(["sudo", "add-apt-repository", "-y", "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"])

#upgrade packages
print("Do you want to install all package updates available? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["sudo", "apt-get", "-y", "upgrade"])

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

#remove unnecessary packages
subprocess.run(["sudo", "apt-get", "-y", "autoremove"])
