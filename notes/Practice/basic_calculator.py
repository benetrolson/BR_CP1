#BHR 2nd basic calculator
number1 = float(input("What is an number? (Do not go too big. )"))
number2 = float(input("What is an number? (Do not go too big. )"))
addition = number1 + number2
subtraction = number1 - number2
exponent = number1 ** number2
multiplaction = number1 * number2
division = number1 / number2
modulo = number1 % number2
int_division = number1 // number2
print(f"{number1} plus {number2} is {addition}. \n{number1} minus {number2} is {subtraction}. \n{number1} times {number2} is {multiplaction}. \n{number1} divided by {number2} is {division}. \nThe remainder of {number1} divided by {number2} is {modulo}. \n{number1} divided by {number2} with no remainder or decimal is {int_division}. \n{number1} to the power of {number2} is {exponent}. ")
