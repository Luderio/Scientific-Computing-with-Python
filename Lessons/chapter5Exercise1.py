count = 0
total = 0

stop = True
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
            print('Invalid Input')
            continue
    else :
        count = count + 1
        total = total + number

average = total / count
print('Total:', total, 'Count:', count, 'Average:', average)
