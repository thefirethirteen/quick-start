# customizations.py
# version 2.3.1

import subprocess
import os

os.chdir("customizations")

#systen76-wallpapers.py
print("Do you want to add system76 wallpapers? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "system76-wallpapers.py"])

#iconpack-obsidian.py
print("Do you want to add iconpack-obsidian? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "iconpack-obsidian.py"])

#fonts-firacode.py
print("Do you want to add firacode fonts? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "fonts-firacode.py"])
