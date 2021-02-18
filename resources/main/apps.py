# apps.py
# version 2.0.0

import subprocess
import os

os.chdir("apps")

#office.sh
print("Do you want to install any office suites? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "office.sh"])

#social.sh
print("Do you want to install any social apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "social.sh"])

#development.sh
print("Do you want to install any development apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "development.sh"])

#streaming.sh
print("Do you want to install any streaming apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "streaming.sh"])

#games.sh
print("Do you want to install any games? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "games.sh"])

#miscellaneous.sh
print("Do you want to install any miscellaneous apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["bash", "miscellaneous.sh"])
