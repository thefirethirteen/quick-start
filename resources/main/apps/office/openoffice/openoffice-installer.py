# openoffice-installer.py
# version 1.0.2

import subprocess
import os

print("What version of Apache OpenOffice do you want to install?")
print("Available versions: 3.4.1; 4.0.0-4.0.1; 4.1.0-4.1.9")
print("Input your desired version:")
VERSION = input()

subprocess.run(["wget", "-O", "download", "https://sourceforge.net/projects/openofficeorg.mirror/files/" + VERSION + "/binaries/en-GB/Apache_OpenOffice_" + VERSION + "_Linux_x86-64_install-deb_en-GB.tar.gz/download"])
subprocess.run(["tar", "-xf", "download"])
os.chdir("en-GB")
os.chdir("DEBS")
os.system("sudo dpkg -i *.deb")
os.chdir("desktop-integration")
os.system("sudo dpkg -i *.deb")
os.chdir("..")
os.chdir("..")
os.chdir("..")
subprocess.run(["rm", "-rf", "download"])
