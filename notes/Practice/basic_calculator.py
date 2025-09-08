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
print(f"{number1:2F} + {number2:2F} = {addition:2F}\n{number1:2F} - {number2:2F} = {subtraction:2F}\n{number1:2F}*{number2:2F} = {multiplaction:2F}\n{number1:2F}/{number2:2F} = {division:2F}\nThe remainder of {number1:2F}/{number2:2F} = {modulo:2F}\nWith no remainder, {number1:2F}/{number2:2F} = {int_division:2F}\n{number1:2F}^{number2:2F} = {exponent:2F}")
