import sys
import os

parent_folder = "/home/jonas/Documents/CTak/daily_programmer"
directory = "c_" + sys.argv[2]
path = os.path.join(parent_folder, directory)

def start():
    #creates a folder with challenge name and creates to empty files
    os.mkdir(path)
    open(path+"/challenge.txt",'a').close()
    open(path+"/solution.py", 'a').close()
    print("Started Challenge %s" % directory)

def solved():
    #checks is challenge exists, if true then it pushes the challenge to GitHub
    if os.path.isdir(path):
        os.system("cd ..")
        os.system("git add %s" % directory)
        os.system("git commit -m 'solved challange %s'" % directory)
        print("Solved and commited %s, need to push to GitHub" % directory)
    else:
        print("%s is not a challenge you started" % directory)

if sys.argv[1] == "start":
    start()
elif sys.argv[1] == "solved":
    solved()
else:
    print("Usage: challenge [start/solved] [challenge no]")