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

# spotify.py

import subprocess
import os

os.system("curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add -")
os.system("echo 'deb http://repository.spotify.com stable non-free' | sudo tee /etc/apt/sources.list.d/spotify.list")

subprocess.run(["sudo", "apt-get", "update"])
subprocess.run(["sudo", "apt-get", "-y", "--install-recommends", "install", "spotify-client"])
