import os
import time

branch = "main"
origin = "https://github.com/elit30/c43.git"
dir = '/mk0'

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
os.system('git push -u origin ' + branch)
time.sleep(5)

# git init
# git add .
# git commit -m "adding files"
# git remote add origin https://github.com/elit30/c43.git
# git push origin main