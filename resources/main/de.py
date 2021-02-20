# de.py
# version 2.1.1

import subprocess
import os

os.chdir("de")

#gnome.py
print("Do you want to install the Gnome Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "gnome.py"])

#mate.py
print("Do you want to install the Mate Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "mate.py"])
