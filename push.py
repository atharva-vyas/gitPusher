import os
import time

gitName = "personal"
dir = '/personal'

branch = "master"

origin = "https://github.com/atharva-vyas/" + str(gitName) +".git"
os.chdir(dir)

os.system('find "/home" -type d -name ".git" -exec rm -rf {} \;')
os.system("cp -r /home " + dir)

def gitReInit():
    print('Do you want to re-initialize git repo? y/n')
    print('WARNING: selecting yes will result in deleting all the previous git branches')
    deleteGitDirectory0 = input("=>")
    if deleteGitDirectory0 == 'y':
        os.system('find "' + dir + '" -type d -name ".git" -exec rm -rf {} \;')
        os.system('git init')
    elif deleteGitDirectory0 == 'n':
        pass
    else:
        print('invalid option')
        gitReInit()
gitReInit()

print('')

os.system('find "' + dir + '" -type d -name "node_modules" -exec rm -rf {} \;')
os.system('git add .')
os.system('git commit -m ' + str(int(time.time())))
os.system('git remote add origin ' + origin)
os.system('git push -u origin ' + branch + ' --force')
