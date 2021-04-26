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

# jetbrains-toolbox.py

import subprocess
import os

print("Getting the JetBrains Toolbox from their website")

# ignoring PEP 8: E501 for now
subprocess.run(["wget", "--output-document=jetbrains-toolbox-1.20.8352.tar.gz", "https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.20.8352.tar.gz"])
subprocess.run(["tar", "--extract", "--file=jetbrains-toolbox-1.20.8352.tar.gz"])

os.chdir("jetbrains-toolbox-1.20.8352")

print("Marking the appimage as executable (a+x)")

subprocess.run(["chmod", "a+x", "jetbrains-toolbox"])
subprocess.run(["./jetbrains-toolbox"])

os.chdir("..")

subprocess.run(["rm", "-f", "jetbrains-toolbox-1.20.8352.tar.gz"])
subprocess.run(["rm", "-r", "-f", "jetbrains-toolbox-1.20.8352"])

print("The Toolbox installs itself in your system and will automatically start with your computer.")
