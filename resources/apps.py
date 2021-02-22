#quick-start - a collection of scripts for a quick start
#Copyright (C) 2021 Andrew F

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

# apps.py
# version 2.8.0

import subprocess
import os

os.chdir("apps")

#browser.py
print("Do you want to install any browsers? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "browser.py"])

#office.py
print("Do you want to install any office suites? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "office.py"])

#social.py
print("Do you want to install any social apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "social.py"])

#streaming.py
print("Do you want to install any streaming apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "streaming.py"])

#games.py
print("Do you want to install any games? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "games.py"])

#development.py
print("Do you want to install any development apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "development.py"])

#miscellaneous.py
print("Do you want to install any miscellaneous apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "miscellaneous.py"])
