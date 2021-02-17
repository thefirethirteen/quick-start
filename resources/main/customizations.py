# customizations.py
# version 1.0.0

import os

os.chdir("customizations")

#systen76-wallpapers.sh
print("Do you want to install system76-wallpapers? [y/n]")
USER_INPUT = input()
if USER_INPUT" == "y":
    os.system("bash system76-wallpapers.sh")

#iconpack-obsidian.sh
print("Do you want to install iconpack-obsidian? [y/n]")
USER_INPUT - input()
if USER_INPUT" == "y":
    os.system("bash iconpack-obsidian.sh")

#fonts-firacode.sh
print("Do you want to install firacode fonts? [Y/n]")
USER_INPUT = input()
if USER_INPUT" == "y":
    os.system("bash fonts-firacode.sh")
