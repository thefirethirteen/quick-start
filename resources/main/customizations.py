# customizations.py
# version 2.4.0

import subprocess
import os

os.chdir("customizations")

#wallpapers.py
print("Do you want to add any wallpapers? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "wallpapers.py"])

#icons.py
print("Do you want to add any icons? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "icons.py"])

#fonts.py
print("Do you want to add any fonts? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "fonts.py"])
