inputArray = []
count = 0
stop = True

#loops to the codeblock below to ask the user to enter a number and appending it to inputArray.
while stop == True :
    inputNumber = input('Enter a number: ')

    try:
        number = float(inputNumber)
    except:
        number = -1

    if number == -1 :
        if inputNumber == 'done' :
            stop = False
            break
        else :
            print('invalid Input')
            continue
    else :
        count = count + 1
        inputArray.append(number)
        continue


#accessing the inputArray to get the min and max values.
min = None
max = None
for items in inputArray :
    if min is None or items < min :
        min = items

    if max is None or items > max :
        max = items

#prints the output once done is entered by the user
print('Minimum:', int(min), 'Maximum:', int(max), 'Count:', count)
