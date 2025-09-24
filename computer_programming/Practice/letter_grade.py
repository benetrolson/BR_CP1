# BHR 2nd what is your grade

while True:
        number_of_grade_input = input("How many times do you want to check your grade? ")
        if number_of_grade_input.isnumeric():
            number_of_grade_input = int(number_of_grade_input)
            if number_of_grade_input > 0 and number_of_grade_input < 100:
                break
            else:
                print("That is invalid. Please try again. ")
        else:
            print("That is invalid. Please try again. ")
while number_of_grade_input:
    while True:
        number_grade = float(input("What is your grade percentage? (Do you not add a percentage.)"))
        if number_grade > 0 and number_grade < 100:
            break
        else:
            print("That is invalid. Please try again. ")
    if number_grade >= 94:
        print("Your grade is A! Good job. Keep up the good work! ")
        number_of_grade_input -= 1
    elif number_grade >= 90:
        print("Your grade is an A-. Do better. ")
        number_of_grade_input -= 1
    elif number_grade >= 87:
        print("Your grade is a B+. You think this is going to cut it? ")
        number_of_grade_input -= 1
    elif number_grade >= 84:
        print("Your grade is a B. Quit while you are ahead. ")
        number_of_grade_input -= 1
    elif number_grade >= 80:
        print("Your grade is a B-. Maybe life is just too hard for you. ")
        number_of_grade_input -= 1
    elif number_grade >= 77:
        print("Your grade is a C+. At this point, just leave the school. ")
        number_of_grade_input -= 1
    elif number_grade >= 74:
        print("Your grade is a C. You are doing great! Keep up the good work. ")
        number_of_grade_input -= 1
    elif number_grade >= 70:
        print("Your grade is a C-. Maybe try something different. ")
        number_of_grade_input -= 1
    elif number_grade >= 67:
        print("Your grade is a D+. How did you do so good? ")
        number_of_grade_input -= 1
    elif number_grade >= 64:
        print("Your grade is a D. Are you sure this is your grade? ")
        number_of_grade_input -= 1
    elif number_grade >= 60:
        print("Your grade is a D-. Maybe change classes. ")
        number_of_grade_input -= 1
    elif number_grade >= 0:
        print("Your grade is an F. You can do it! ")
        number_of_grade_input -= 1
    else:
        print("How did you get here? ")
#A94 A-90 B+87 B84 B-80 C+77 C74 C-70 D+67 D64 D-60 F0
