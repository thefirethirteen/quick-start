# icons.py
# version 1.0.0

import subprocess
import os

os.chdir("icons")

#iconpack-obsidian.py
print("Do you want to add iconpack-obsidian? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "iconpack-obsidian.py"])
