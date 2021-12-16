"""
/ / / / / / / / / /
dirNavigate.py v0.1.0
/ / / / / / / / / /
Version Notes
-------------
0.1.0 Generic python script that works with the os library to navigate or display
    items in a directory.
"""

import os



def main():
    cwd = workingDirectory()
    exit()

def workingDirectory():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cwd = os.getcwd()
    print("Current directory is: ", cwd)
    displayWorkingDir()
    return cwd

def displayWorkingDir():
    print("Files in this directory are:")
    for i in os.scandir():
        if i.is_file():
            print(i.name)

#Keeps the script from autoclosing after running. Disable by not calling.
def exit():
	k = 0
	while k != '1':
		k = input("Press 1 to exit: ")
		print(k)

if __name__ == "__main__":
	main()
