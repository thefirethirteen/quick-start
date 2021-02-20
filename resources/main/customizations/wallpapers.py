# wallpapers.py
# version 1.0.0

import subprocess
import os

os.chdir("wallpapers")

#systen76-wallpapers.py
print("Do you want to add system76 wallpapers? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "system76-wallpapers.py"])
