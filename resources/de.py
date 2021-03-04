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

# de.py
# version 2.2.0

import subprocess
import os

os.chdir("de")

# gnome.py
print("Do you want to install the Gnome Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "gnome.py"])

# mate.py
print("Do you want to install the Mate Desktop Environment? [y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "mate.py"])
