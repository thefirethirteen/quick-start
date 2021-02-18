# customizations.py
# version 2.1.0

import subprocess
import os

os.chdir("customizations")

#systen76-wallpapers.sh
print("Do you want to install system76-wallpapers? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "system76-wallpapers.py"])

#iconpack-obsidian.sh
print("Do you want to install iconpack-obsidian? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "iconpack-obsidian.sh"])

#fonts-firacode.sh
print("Do you want to install firacode fonts? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "fonts-firacode.sh"])
