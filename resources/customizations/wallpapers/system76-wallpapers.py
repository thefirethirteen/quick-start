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

# system76-wallpapers.py

import subprocess

subprocess.run(["sudo", "apt-add-repository", "-y", "-s", "ppa:system76-dev/stable"])

subprocess.run(["sudo", "apt-get", "update"])

subprocess.run(["sudo", "apt-get", "-y", "install", "system76-wallpapers"])
