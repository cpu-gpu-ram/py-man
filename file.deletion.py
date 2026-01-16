import os

target = input("Name of file? (this includes the extensions)")
if os.path.exists(target):
    confirmation = input('File has been found.'
                         'Do you really wish to terminate this file?'
                         'y/n').lower().strip()
    if confirmation == "y":
        os.remove(target)
        print(f"{target} Has been terminated")
    else:
        print(f"{target} Has not been terminated")
else:
    print("File not found.")