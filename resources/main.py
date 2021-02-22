#quick-start - a collection of scripts for a quick start
#Copyright (C) 2021 Andrew F

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

# main.py
# version 2.1.0

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

#quick-start-addons
os.chdir("..")
os.chdir("..")
if os.path.isfile("addons.py"):
    print("Addons detected!")
    subprocess.run(["python3", "addons.py"])
else:
    print("No quick-start addons detected!")

#upgrade packages
print("Do you want to install all package updates available? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["sudo", "apt-get", "-y", "upgrade"])

#remove unnecessary packages
subprocess.run(["sudo", "apt-get", "-y", "autoremove"])
