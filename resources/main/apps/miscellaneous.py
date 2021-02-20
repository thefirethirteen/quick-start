# miscellaneous.py
# version 1.1.1

import subprocess
import os

os.chdir("miscellaneous")

#wine.py
print("Do you want to install wine? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "wine.py"])
