# development.py
# version 1.1.1

import subprocess
import os

os.chdir("development")

#codeblocks.py
print("Do you want to install Code::Blocks? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "codeblocks.py"])
