# development.py
# version 1.0.0

import subprocess
import os

os.chdir("development")

#codeblocks.sh
print("Do you want to install Code::Blocks? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "codeblocks.sh"])
