import string
import random
import os

  
cdir = os.getcwd()
name = 'passwords.txt'


def generate():
    charcount = 0   
    characters = [] 
    isWrite = True
    symbolsAllowed = False
    symbols = ['!', '?', '$', '&', '#', '@']
    symbolsCustom = []
    useCustom = False

    for root, dirs, files in os.walk(cdir):
        for items in files:
            if items == name:
                isWrite = False

    if isWrite == True:
        log = open('passwords.txt', 'w')
    elif isWrite == False:
        log = open('passwords.txt', 'a')

    toWrite = []
    os.system('cls')
    passLength = int(input('Enter the length of password you want: '))
    passType = input('What will this password be used for?: ')
    toWrite.append(passType)
    symAllowed = input('Are symbols allowed? (Y/N): ')
    
    if symAllowed.upper() == 'Y':
        symbolsAllowed = True
        os.system('cls')
        useCustomQ = input('Would you like to use the default symbols(1), or input a custom list(2)?: ')
        if useCustomQ == '1':
            useCustom == False
        elif useCustomQ == '2':
            useCustom = True
            customSymbols = input('Enter your custom list of symbols with no spaces: ')
            symbolsCustom = customSymbols.split(', ')
    elif symAllowed.upper() == 'N':
        symbolsAllowed = False
    
    while charcount < passLength: 
        if symbolsAllowed == True:
            charType = random.randint(1, 3) 
            if charType == 1:
                characters.append(str(random.randint(0, 9)))
                charcount = charcount + 1
            elif charType == 2:
                characters.append(random.choice(string.ascii_letters))
                charcount = charcount + 1
            elif charType == 3:
                if useCustom == False:
                    characters.append(random.choice(symbols))
                    charcount = charcount + 1
                elif useCustom == True:
                    randomChar = random.choice(customSymbols)
                    if randomChar == ' ':
                        print('SPACE ERROR')
                    else:
                        characters.append(randomChar)
                    charcount += 1
        elif symbolsAllowed == False:
            charType = random.randint(1, 2) 
            if charType == 1:
                characters.append(str(random.randint(0, 9)))
                charcount = charcount + 1
            elif charType == 2:
                characters.append(random.choice(string.ascii_letters))
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
