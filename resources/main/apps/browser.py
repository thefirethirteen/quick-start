# browser.py
# version 1.1.0

import subprocess
import os

os.chdir("browser")

#firefox.sh
print("Do you want to install Firefox? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "firefox.py"])
