# games.py
# version 1.0.0

import subprocess
import os

os.chdir("games")

#steam.sh
print("Do you want to install Steam? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "steam.sh"])
