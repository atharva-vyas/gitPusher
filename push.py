import os
import time

gitName = "personal"
dir = '/personal/home/'

branch = "master"

origin = "https://github.com/atharva-vyas/" + str(gitName) +".git"
os.chdir(dir)

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

def gitInit():
    print("this will push the latest version of /personal directory to your git repository")
    print("Choose no if you dont know what to do, git init will wipe out all previous branches")
    gitInit0 = input("git init? y/n \n=> ")

    if gitInit0 == 'y':
        os.system('git init')
    elif gitInit0 == 'n':
        pass
    else:
        os.system('clear')
        print('invalid option')
        gitInit()
# gitInit()

print('')

os.system('find "' + dir + '" -type d -name "node_modules" -exec rm -rf {} \;')
os.system('git add .')
os.system('git commit -m ' + str(int(time.time())))
os.system('git remote add origin ' + origin)
os.system('git push -u origin ' + branch + ' --force')
