

def mainmess():
    global a
    b = input("1 | Zip Cracker\n2 | ....\n\n\n~~ ") 
    if b in a:
        print("Chargement...")
        answer = b
    else:
        print("Mauvais choix !")
        return mainmess()

if __name__ == '__main__':
    a = ['1','2','3','4']
    print('_______Tools v1_______\n\n\n\n')
    mainmess()



