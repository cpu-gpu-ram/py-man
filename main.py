import os
while True:
    print('Please click the number that corresponds with the function you would like to do')
    print('1. Create a .txt File')
    print('2. Create a folder.')
    print('3. Delete a file ')
    print('4. Delete an empty Folder')
    print('5. Os Checker.')
    print('6. Start Network Manager GUI.')
    print('7. Watch anime (dub)')
    print('8. Quit')
    usrinput = input ()
    if usrinput == '1':
        print('Option 1 Chosen.')
        os.system('python txt.Func.py')
    elif usrinput == '2':
        print('Option 2')
        os.system('python folder.func.py')
    elif usrinput == '3':
        print('Option 3')
        os.system('python file.deletion.py')
    elif usrinput == '4':
        print('Option 4')
        os.system('python folder.deletion.py')
    elif usrinput == '5':
        print('Option 5')
        os.system('python os.checker.py')
    elif usrinput == '6':
        print('Option 6')
        os.system('python NM.gui.py')
    elif usrinput == '7':
        print('Option 7')
        os.system('python Anime.py')
    elif usrinput == '8':
        exit
    else :
        print ("invaid input")
