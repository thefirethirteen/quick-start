# de.py
# version 1.0.3

import os

os.chdir("de")

#mate.sh
print("Do you want to install the Mate Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash mate.sh")

#gnome.sh
print("Do you want to install the Gnome Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash gnome.sh")
