# games.py
# version 1.1.1

import subprocess
import os

os.chdir("games")

#steam.py
print("Do you want to install Steam? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "steam.py"])
