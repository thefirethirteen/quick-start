# streaming.py
# version 1.1.0

import subprocess
import os

os.chdir("streaming")

#spotify.sh
print("Do you want to install Spotify? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "spotify.py"])