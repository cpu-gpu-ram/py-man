txtname = input('Name ? ')
if not txtname.lower().endswith('.txt'):
    txtname += '.txt'

    with open(txtname, "x") as file:
        file.write("")
        print ('done')