import os
tar_fold = input('Name of folder? ')
if os.path.exists(tar_fold):
    confirmation2 = input('Directory has been found.'
                          'Do you really wish to terminate this file?'
                          'y/n').lower().strip()
    if confirmation2 == "y":
        os.removedirs(tar_fold)
        print(f"{tar_fold} Has been terminated")
    else:
        print(f"{tar_fold} Has not been terminated")
else:
    print("Folder not found.")
