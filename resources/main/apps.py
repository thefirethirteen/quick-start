# apps.py
# version 1.0.1

import os

os.chdir("apps")

#office.sh
print("Do you want to install any office suites? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash office.sh")

#social.sh
print("Do you want to install any social apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash social.sh")

#development.sh
print("Do you want to install any development apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash development.sh")

#streaming.sh
print("Do you want to install any streaming apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash streaming.sh")

#games.sh
print("Do you want to install any games? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash games.sh")

#miscellaneous.sh
print("Do you want to install any miscellaneous apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    os.system("bash miscellaneous.sh")
