# main.py
# version 1.1.0

import os

os.chdir("main")

print("This script will install desktop environments, apps, customizations and copy app configs.")
print("Do you want to continue? [Y/n]")

USER_INPUT = input()

if USER_INPUT == "y":
    #update package database
    os.system("sudo apt-get update")

    #required repositories
    os.system('sudo add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) main universe restricted multiverse"')

    #package update
    print("Do you want to install all package updates available? [Y/n]")
    USER_INPUT = input()
    if USER_INPUT == "y":
        os.system("sudo apt-get -y upgrade --allow-downgrades")

    #runtimes.sh
    print("Do you want to install any runtimes? [Y/n]")
    USER_INPUT = input()
    if USER_INPUT == "y":
        os.system("bash runtimes.sh")

    #de.sh
    print("Do you want to install any desktop environments? [y/N]")
    USER_INPUT = input()
    if USER_INPUT == "y":
        os.system("bash de.sh")

    #apps.sh
    print("Do you want to install any apps? [Y/n]")
    USER_INPUT = input()
    if USER_INPUT == "y":
        os.system("python apps.py")

    #customizations.sh
    print("Do you want to install any customizations? [Y/n]")
    USER_INPUT = input()
    if USER_INPUT == "y":
        os.system("bash customizations.sh")

    #remove unnecessary packages
    os.system("sudo apt-get -y autoremove")

#echo -e "\e[1;33mAfter restarting, start [next_script_name].sh using start.sh  \e[0m"
