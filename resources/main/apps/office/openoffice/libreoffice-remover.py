# libreoffice-remover.py
# version 1.0.0

import subprocess
import os

os.system("sudo apt-get -y remove libreoffice*")
subprocess.run(["sudo", "apt-get", "-y", "autoremove"])
