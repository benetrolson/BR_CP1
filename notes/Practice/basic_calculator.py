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
print(f"{number1} + {number2} = {addition}\n{number1} - {number2} = {subtraction}\n{number1}*{number2} = {multiplaction}\n{number1}/{number2} = {division}\nThe remainder of {number1}/{number2} = {modulo}\nWith no remainder, {number1}/{number2} = {int_division}\n{number1}^{number2} = {exponent}")
