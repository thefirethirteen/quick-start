# codeblocks.py
# version 1.0.0

import subprocess

subprocess.run(["sudo", "add-apt-repository", "-y", "ppa:codeblocks-devs/release"])
subprocess.run(["sudo", "apt-get", "update"])

subprocess.run(["sudo", "apt-get", "-y", "install", "codeblocks", "codeblocks-contrib"])

subprocess.run(["sudo", "add-apt-repository", "-y", "-r", "ppa:codeblocks-devs/release"])
