fNameInput = input('Enter a file name: ')

try :
    fileName = open(fNameInput)
except :
    print(fNameInput, 'is not existing')
    quit()

for lines in fileName :
    lines = lines.rstrip()
    print(lines.upper())