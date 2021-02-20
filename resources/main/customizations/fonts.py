# fonts.py
# version 1.0.0

import subprocess
import os

os.chdir("fonts")

#fonts-firacode.py
print("Do you want to add firacode fonts? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "fonts-firacode.py"])
