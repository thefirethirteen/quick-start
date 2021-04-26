# quick-start - a collection of scripts for a quick start
# Copyright (C) 2021 thefirethirteen

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

# codeblocks.py

import subprocess

print("Adding Code::Blocks' ppa")

subprocess.run(["sudo", "add-apt-repository", "--no-update", "--yes", "ppa:codeblocks-devs/release"])
subprocess.run(["sudo", "apt-get", "update"])

print("Installing Code::Blocks")

subprocess.run(["sudo", "apt-get", "--yes", "install", "codeblocks", "codeblocks-contrib"])

print("Removing Code::Blocks' ppa")

subprocess.run(["sudo", "add-apt-repository", "--remove", "--yes", "ppa:codeblocks-devs/release"])
