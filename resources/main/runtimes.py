# runtimes.py
# version 2.0.0

import subprocess
import os

os.chdir("runtimes")

#java.sh
print("Do you want to install java? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "java.sh"])
