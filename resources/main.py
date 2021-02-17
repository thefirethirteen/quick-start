# main.py
# version 1.4.0

import os

os.chdir("main")

#update package database
os.system("sudo apt-get update")

#add required repositories
os.system('sudo add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"')

#upgrade packages
print("Do you want to install all package updates available? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("sudo apt-get -y upgrade --allow-downgrades")

#runtimes.py
print("Do you want to install any runtimes? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("python3 runtimes.py")

#de.py
print("Do you want to install any desktop environments? [y/N]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("python3 de.py")

#apps.py
print("Do you want to install any apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("python3 apps.py")

#customizations.py
print("Do you want to install any customizations? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("python3 customizations.py")

#remove unnecessary packages
os.system("sudo apt-get -y autoremove")
