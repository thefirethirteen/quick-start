# iconpack-obsidian.py
# version 1.1.1

import subprocess
import os

subprocess.run(["git", "clone", "https://github.com/madmaxms/iconpack-obsidian"])

os.chdir("iconpack-obsidian")
os.system("sudo mv Obsidian* /usr/share/icons")
os.chdir("..")

subprocess.run(["rm", "-r", "-f", "iconpack-obsidian"])
