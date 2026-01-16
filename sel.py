import platform
import os

while True:
    print ('Hello Friend What are we doing today ? ')
    print('Type the corrisponding number with the function you want to do else type exit to leave')
    print ('1. Create a .txt')
    print ('2. OS Checker')
    print ('3. Delete a File.')
    print ('4. Delete a folder and everything inside.')
    print ('5. Create a folder.')
    print ('6. GUI based network manager.')
    print ('7. Watch some dub anime.')

    usrinput = input().strip().lower()

    if usrinput == 'exit':
        print('Goodbye LOL')
        break
    if usrinput == '1' :
        txtname = input('Name ? ')
        if not txtname.lower().endswith('.txt'):
            txtname += '.txt'

        with open(txtname, "x") as file:
            file.write("")
            print ('done')

    elif usrinput == '2' :
        print ('Searching ----------------')
        print ('Here:')
        print ({platform.system()})
        print (f'version = {platform.release()}')
        print(f"{platform.machine()}")

    elif usrinput == '3'  :
        target = input("Name of file? (this includes the extensions)")
        if os.path.exists(target):
            confirmation  = input('File has been found.'
                   'Do you really wish to terminate this file?'
                   'y/n').lower().strip()
            if confirmation == "y":
                os.remove(target)
                print(f"{target} Has been terminated")
            else :
                print(f"{target} Has not been terminated")
        else:
            print("File not found.")

    elif usrinput == '4' :
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

    elif usrinput == '5' :
        folder =  input('Name ? ')
        os.mkdir(folder)
        print(f'{folder} Is now a directory')

    elif usrinput == '6' :
        print ('launching nm')
        os.execvp("nmtui", ["nmtui"])

    elif usrinput == '7' :
        print('enjoy')
        os.system("ani-cli --dub")

    else:
        print("invalid input")