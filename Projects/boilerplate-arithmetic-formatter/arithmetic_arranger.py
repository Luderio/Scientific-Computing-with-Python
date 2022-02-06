import re

def arithmetic_arranger(problems, solved=False) :
  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""

  #checks for the length of the list. (list length should not be more than 5)
  if len(problems) > 5 :
    return "Error: Too many problems."

  for items in problems :

    #list value validation will return an error if the list contains unacceptable format and characters
    if re.search('[^\s0-9.+-]', items) :
      if re.search('[/]', items) or re.search('[*]', items) :
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."
    
    firstNumber = items.split(" ")[0]
    operator = items.split(" ")[1]
    secondNumber = items.split(" ")[2]

    if len(firstNumber) >= 5 or len(secondNumber) >= 5 :
      return "Error: Numbers cannot be more than four digits."
    
    #will compute for the result of the operations (add or minus)
    result = ""
    if (operator == '+') :
      result = str(int(firstNumber) + int(secondNumber))
    elif (operator == "-") :
      result = str(int(firstNumber) - int(secondNumber))

    #will format the output as per the rules.
    length = max(len(firstNumber), len(secondNumber)) + 2
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = ""
    res = str(result).rjust(length)
    for s in range(length) :
      line += "-"
    
    if items != problems[-1] :
      first += top + "    "
      second += bottom + "    "
      lines += line + "    "
      sumx += res + "    "
    else :
      first += top
      second += bottom
      lines += line
      sumx += res
    
  if solved :
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else :
    string = first + "\n" + second + "\n" + lines

  return string