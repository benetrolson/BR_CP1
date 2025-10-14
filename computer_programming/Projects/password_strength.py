#BHR 2nd password strength checker


#loop
while True:
    #reset the strength to 0
    strength = 0
    #reset all the variables to false
    up = False
    low = False
    num = False
    #ask if the user wants to quit 
    check = input("Do you want to quit? If so, please write \"q\". If not, feel free to write anything. ")
    #if they want to quit
    if check == "q":
        #end the loop
        break
    #easter eggs
    elif check == "anything":
        strength += 5
    elif check == "hello":
        strength -= 105
    elif check == "Eve is the best. ":
        strength = '"Plus two million points"'
    #Ask the user for the password
    password = input("Please write your prospective password. ")
    #if it is longer than 7 letters
    if len(password) > 7:
        #add 1 to the password strength
        strength += 1
    #otherwise
    else:
        #say that they need to make their password longer
        print("You need to make your password longer. ")
    #looping through every single letter
    for letter in password:
        #check if that letter is uppercase
        if letter.isupper():
            #make it so that the information that it is uppercase is true
            up = True
        #if it is true
    if up:
            #add 1 to the password strength
        strength += 1
        #otherwise
    else:
            #say that they have to add an uppercase letter
        print("You need to add an uppercase letter. ")
    #looping through every single letter
    for letter in password:
    #check if that letter is lowercase
        if letter.islower():
            #make it so that the information that it is lowercase is true
            low = True
    #if it is true
    if low:
        #add 1 to the password strength
        strength += 1
    #otherwise
    else:
        #say that they have to add an lowercase letter
        print("You need to add a lowercase letter. ")
    #check if the string is not alpha numeric (isalnum)
    if not password.isalnum() and password:
        #add 1 to the password strength
        strength += 1
    #otherwise
    else:
        #say that they need to add a special character
        print("You need to add a special character. ")
    #looping through every single letter
    for letter in password:
        #check if that letter is numeric
        if letter.isdigit():
            #if it is, make it so that the information that there is a number is true
            num = True
    #if it is true
    if num:
        #add 1 to the password strength
        strength += 1
    #otherwise
    else:
        #say that they have to add an number
        print("You need to add a number. ")
    #display the password strength
    print(f"Your password strength is {strength}/5. ")
    if strength == 5:
        print("That is very strong. Good job! ")
    elif strength == 4:
        print("This is strong but you can do better. ")
    elif strength == 3:
        print("Your password is moderate. You have room to improve. ")
    elif strength == 1 or strength == 2:
        print("Your password is weak. Do better. ")
    else:
        print("You found the easter egg! Don't use it again. ")

