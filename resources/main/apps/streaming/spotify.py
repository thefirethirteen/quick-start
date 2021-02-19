# spotify.py
# version 1.0.0

import subprocess
import os

os.system("curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add -")
os.system("echo 'deb http://repository.spotify.com stable non-free' | sudo tee /etc/apt/sources.list.d/spotify.list")

subprocess.run(["sudo", "apt-get", "update"])
subprocess.run(["sudo", "apt-get", "-y", "install", "spotify-client"])
