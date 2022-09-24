import os
import time

branch = "master"
dir = 'gitPusher'

origin = "https://github.com/elit30/" + str(dir) +".git"
os.chdir(os.getcwd() + "/" + dir)

os.system('git init')
os.system('git add .')
os.system('git commit -m ' + str(int(time.time())))
os.system('git remote add origin ' + origin)
os.system('git push -u origin ' + branch)
