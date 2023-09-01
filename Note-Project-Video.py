import sys
#Note List

def mainMenu():
    global optionSelect
    print('Welcome to Notes++!')
    print('1. Get started with your notes!')
    print('2. Open you\'re notes!')
    print('3. Exit program')
    optionSelect = input()
    return optionSelect

noteList = []

try:
    with open('notes.txt', 'r') as file:
        noteList = file.read().splitlines()
    
except FileNotFoundError:
    pass


while True:
    mainMenu()
    if optionSelect in {'1','2'}:
        print('Tpye exit to exit!')
    while True:
        if optionSelect == '1':
            print('Tpye anyting to enter a note!')
            noteInput = input()
            if noteInput.lower() == 'exit':
                print('Did you want to exit? (yes/no)')
                exitValidation = input()
                if exitValidation.lower() == 'yes' or 'y':
                    break
                elif exitValidation.lower() == 'no' or 'n':
                    continue
            noteList.append(noteInput)
            print(noteList)
            

        elif optionSelect == '2':
            print('Your current notes:')
            for note in noteList:
                print(f'-{note}')
            exitInput = input()
            if exitInput.lower() == 'exit':
                if exitInput.lower() == 'exit':
                    print('Did you want to exit? (yes/no)')
                    exitValidation = input()
                    if exitValidation.lower() == 'yes' or 'y':
                        break
                    elif exitValidation.lower() == 'no' or 'n':
                        continue

        elif optionSelect == '3':
            print('Saving your file!')
            with open('notes.txt', 'w') as file:
                for note in noteList:
                    file.write(note + '\n')
            print('Goodbye!')
            sys.exit()




