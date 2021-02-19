# wine.py
# version 1.0.0

import subprocess
#import os

subprocess.run(["sudo", "dpkg", "--add-architecture", "i386"])

subprocess.run(["wget", "-nc", "https://dl.winehq.org/wine-builds/winehq.key"])
subprocess.run(["sudo", "apt-key", "add", "winehq.key"])
subprocess.run(["rm", "-f", "winehq.key"])

subprocess.run(["sudo", "add-apt-repository", "-y", "deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main"])
#os.system("sudo add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ groovy main'")
sudo apt-get update

sudo apt-get -y install --install-recommends winehq-stable
