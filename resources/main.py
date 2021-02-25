# quick-start - a collection of scripts for a quick start
# Copyright (C) 2021 Andrew F

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# main.py

import subprocess
import os

# add required repositories
subprocess.run(["sudo", "add-apt-repository", "-y", "--no-update", "universe"])
subprocess.run(["sudo", "add-apt-repository", "-y", "--no-update", "multiverse"])
subprocess.run(["sudo", "add-apt-repository", "-y", "--no-update", "restricted"])

# update package database
subprocess.run(["sudo", "apt-get", "update"])

# fix broken packages
subprocess.run(["sudo", "apt-get", "--fix-broken", "-y", "install"])

# install required packages
subprocess.run(["sudo", "apt-get", "-y", "install", "curl"])

# runtimes.py
print("Do you want to install any runtimes? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "runtimes.py"])

# de.py
print("Do you want to install any desktop environments? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "de.py"])

# apps.py
print("Do you want to install any apps? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "apps.py"])

# customizations.py
print("Do you want to install any customizations? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "customizations.py"])

# addons.py (quick-start-addons)
os.chdir("..")
if os.path.isfile("addons.py"):
    print("Addons detected!")
    subprocess.run(["python3", "addons.py"])
else:
    print("No quick-start addons detected!")

# upgrade packages
print("Do you want to install all package updates available? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["sudo", "apt-get", "-y", "upgrade"])

# fix broken packages
subprocess.run(["sudo", "apt-get", "--fix-broken", "-y", "install"])

# remove unnecessary packages
subprocess.run(["sudo", "apt-get", "-y", "autoremove"])
