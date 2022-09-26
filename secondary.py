import string
import random
import os

symbols = ['!', '?', '$', '&', '#', '@']  

def generate():
    charcount = 0   
    characters = [] 
    log = open('Password Generators\V3\passwords.txt', 'a')
    toWrite = []
    os.system('cls')
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
