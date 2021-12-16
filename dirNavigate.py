"""
/ / / / / / / / / /
dirNavigate.py v0.1.0
/ / / / / / / / / /
Version Notes
-------------
0.1.0 Generic python script that works with the os library to navigate or display
    items in a directory. Asks user for file extension they'd like to save and if
    that extension exists, it'll save that result to a dictionary.
"""
import os

def main():
    print("Current directory is: ", workingDirectory())
    displayFilesInDir()
    ext = askFileExtension()
    files2save = scanFileExtensions(workingDirectory(), ext) #Returns as a list
    print(type(files2save))
    exit() #Disable by commenting out

# Define current path
def workingDirectory():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    cwd = os.getcwd()
    return cwd

# Print the files in the current directory
def displayFilesInDir():
    allFiles = []
    print("Files in this directory are:")
    for i in os.scandir():
        if i.is_file():
            allFiles.append(i.name)
            print(i.name)

# Ask user for extension to type to save
def askFileExtension():
    answer = input("What extensions do you want to save? ")
    dot  = "."
    if dot in answer:
        print("Extensions to be saved: ", answer)
    else:
        answer = dot + answer
        print("Extension to be saved: ", answer)
    #print(type(answer))
    return answer

# After taking user input, scan the working directory for files with that extension.
# If files exist, append to a list and return the result
def scanFileExtensions(cwd, answer):
    extensionFilenames = []
    for root, dirs, files in os.walk(cwd):
        for file in files:
            if file.endswith(answer):
                print(file)	#Print json filenames here if you need to debug
                extensionFilenames.append(file)
        if len(extensionFilenames) == 0:
            print("There are no files with the %s extension." % answer)
            break
    return extensionFilenames

#Keeps the script from autoclosing after running. Disable by not calling.
def exit():
    k = 0
    while k != '1':
        k = input("Press 1 to exit: ")
        print(k)

if __name__ == "__main__":
    main()
