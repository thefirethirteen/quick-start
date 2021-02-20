# libreoffice-remover.py
# version 1.0.2

import subprocess

subprocess.run(["sudo", "apt-get", "-y", "remove", 'libreoffice*'])
subprocess.run(["sudo", "apt-get", "-y", "autoremove"])
