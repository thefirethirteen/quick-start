# office.py
# version 1.1.0

import subprocess
import os

os.chdir("office")

#openoffice.sh
print("Do you want to install Apache OpenOffice? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "openoffice.py"])
