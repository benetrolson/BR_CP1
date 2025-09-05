#BHR 2nd Idiot Proof
name = input("What is your name? ").strip().title()
number = input("What is your number? ")
grade_average = float(input("What is your grade point average? "))
number1 = number[:3]
number2 = number[3:6]
number3 = number[6:]
correct_number = number1 + " " + number2 + " " + number3
correct_average = round(grade_average, 1)
if grade_average >= 4:
	grade_average = 4.0
print(f"Your name is {name}, your number is {correct_number}, and your grade average is {correct_average}. ")
