# openoffice.py
# version 1.0.0

import subprocess
import os

os.chdir("openoffice")

print("Warning: Installing Apache OpenOffice will remove LibreOffice!")
print("Do you want to continue? [y/n]")

USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "libreoffice-remover.py"])
    subprocess.run(["python3", "openoffice-installer.py"])
