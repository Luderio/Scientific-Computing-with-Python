from audioop import reverse


wordCounter = dict()

while True :
    inputFile = input('Enter a file: ')
    try :
        fileName = open(inputFile)
    except :
        fileName = 'invalid'
    
    if fileName == 'invalid' :
        if inputFile == 'done' :
            break
        else :
            print('Invalid Input')
            continue
    
    for lines in fileName :
        lines = lines.rstrip()
        words = lines.split()
        for wordItems in words :
            wordCounter[wordItems] = wordCounter.get(wordItems, 0) + 1
    
    lst = list()
    for (key,value) in wordCounter.items() :
        revtup = (value, key)
        lst.append(revtup)
    
    lst = sorted(lst, reverse=True)
    
    sortedByValue = list()
    for (value, key) in lst :
        newtup = (key, value)
        sortedByValue.append(newtup)
    
    print('Largest Word:', lst[0][1], 'Count:', lst[0][0])
    print(wordCounter)
    continue
