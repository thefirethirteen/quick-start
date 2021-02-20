# browser.py
# version 1.1.1

import subprocess
import os

os.chdir("browser")

#firefox.py
print("Do you want to install Firefox? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "firefox.py"])
