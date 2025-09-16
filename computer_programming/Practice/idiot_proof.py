#BHR 2nd Idiot Proof
while True:
    name = input("What is your name? ").strip()
    if not name.isdigit() and name.istitle():
        break
    else:
        print("Your name is invalid. Please try again. ")
while True:
    number = input("What is your number? ")
    if len(number) == 10 and number.isdigit() and not " " in number:
        break
    else:
        print("That is invalid. Please try again. ")
number1 = number[:3]
number2 = number[3:6]
number3 = number[6:]
correct_number = number1 + " " + number2 + " " + number3
while True:
    grade_average = float(input("What is your grade point average? "))
    if grade_average >= 4.01 or grade_average < -0.01:
        print("That is an invalid GPA. Please try again. ")
    else:
	    break
correct_average = round(grade_average, 1)
print(f"Your name is {name}, your number is {correct_number}, and your grade average is {correct_average}. ")