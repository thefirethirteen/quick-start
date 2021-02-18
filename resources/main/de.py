# de.py
# version 2.0.0

import subprocess
import os

os.chdir("de")

#mate.sh
print("Do you want to install the Mate Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "mate.sh"])

#gnome.sh
print("Do you want to install the Gnome Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "gnome.sh"])
