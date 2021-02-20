# apps.py
# version 2.7.0

import subprocess
import os

os.chdir("apps")

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

#development.py
print("Do you want to install any development apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "development.py"])

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

#miscellaneous.py
print("Do you want to install any miscellaneous apps? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "miscellaneous.py"])

#browser.py
print("Do you want to install any browsers? [Y/n]")
USER_INPUT = input()
if USER_INPUT == "y":
    subprocess.run(["python3", "browser.py"])
