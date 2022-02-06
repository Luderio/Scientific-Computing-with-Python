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
    
    largestWordCount = None
    largestWord = None
    for word,count in wordCounter.items() :
        if largestWordCount is None or count > largestWordCount :
            largestWord = word
            largestWordCount = count
    print('Largest Word:', largestWord, 'Count:', largestWordCount)
    print(wordCounter)
    continue

