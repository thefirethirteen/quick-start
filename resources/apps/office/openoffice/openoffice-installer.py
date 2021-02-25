# quick-start - a collection of scripts for a quick start
# Copyright (C) 2021 Andrew F

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# openoffice-installer.py

import subprocess
import os

print("What version of Apache OpenOffice do you want to install?")
print("Available versions: 3.4.1; 4.0.0-4.0.1; 4.1.0-4.1.9")
print("Input your desired version:")
VERSION = input()

subprocess.run(["wget", "-O", "openoffice-download", "https://sourceforge.net/projects/openofficeorg.mirror/files/" + VERSION + "/binaries/en-GB/Apache_OpenOffice_" + VERSION + "_Linux_x86-64_install-deb_en-GB.tar.gz/download"])
subprocess.run(["tar", "-xf", "openoffice-download"])

os.chdir("en-GB")
os.chdir("DEBS")

os.system("sudo dpkg -i *.deb")

os.chdir("desktop-integration")

os.system("sudo dpkg -i *.deb")

os.chdir("..")
os.chdir("..")
os.chdir("..")

subprocess.run(["rm", "-f", "openoffice-download"])
subprocess.run(["rm", "-r", "-f", "en-GB"])
