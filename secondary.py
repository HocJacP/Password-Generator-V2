from asyncio.windows_events import NULL
import string
import random
import os

symbols = ['!', '?', '$', '&', '#', '@']  
dir = os.getcwd()
name = 'passwords.txt'


def generate():
    charcount = 0   
    characters = [] 

    for files in os.walk(dir):
        for items in files:
            if name in items:
                log = open(name, 'a')
                isWrite = False
            elif name not in items:
                log = open(name, 'w')
                isWrite = True
            
    toWrite = []
    os.system('cls')
    print(isWrite)
    passLength = int(input('Enter the length of password you want: '))
    passType = input('What will this password be used for?: ')  
    toWrite.append(passType)

    while charcount < passLength: 
        charType = random.randint(1, 3) 
        if charType == 1:
            characters.append(str(random.randint(0, 9)))
            charcount = charcount + 1
        elif charType == 2:
            characters.append(random.choice(string.ascii_letters))
            charcount = charcount + 1
        elif charType == 3:
            characters.append(random.choice(symbols))
            charcount = charcount + 1

    finalPass = "".join(characters) 
    toWrite.append(finalPass)
    toWrite.append('\n')
    log.writelines('\n'.join(toWrite))
    log.close
    os.system('cls')
    print('Your new password is: ')
    print(finalPass)
    print('Run the program again to generate a new password.')
