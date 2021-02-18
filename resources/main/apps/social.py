# social.py
# version 1.0.1

import subprocess
import os

os.chdir("social")

#discord.sh
print("Do you want to install discord? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "discord.sh"])
