# system76-wallpapers.py
# version 1.0.0

import subprocess

subprocess.run(["sudo", "apt-add-repository", "-y", "-s", "ppa:system76-dev/stable"])

subprocess.run(["sudo", "apt-get", "update"])

subprocess.run(["sudo", "apt-get", "-y", "install", "system76-wallpapers"])
