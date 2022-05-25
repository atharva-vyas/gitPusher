import os
import time
from venv import main

branch = "master"
origin = "https://github.com/elit30/c43.git"
dir = '/mk0'

if branch == "main":
    os.chdir(os.getcwd() + dir)
    time.sleep(5)
    os.system('git init')
    time.sleep(5)
    os.system('git add .')
    time.sleep(5)
    os.system('git commit -m ' + str(int(time.time())))
    time.sleep(5)
    os.system('git branch -M main')
    time.sleep(5)
    os.system('git remote add origin ' + origin)
    time.sleep(5)
    os.system('git push -u origin main')
    time.sleep(5)

if branch == "master":
    os.chdir(os.getcwd() + dir)
    time.sleep(5)
    os.system('git init')
    time.sleep(5)
    os.system('git add .')
    time.sleep(5)
    os.system('git commit -m ' + str(int(time.time())))
    time.sleep(5)
    os.system('git remote add origin ' + origin)
    time.sleep(5)
    os.system('git push origin ' + branch)
    time.sleep(5)

# git init
# git add .
# git commit -m "adding files"
# git remote add origin https://github.com/elit30/c43.git
# git push origin main