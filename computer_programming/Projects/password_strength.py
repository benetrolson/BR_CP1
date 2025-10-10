#BHR 2nd password strength checker


#loop
while True:
    #reset the strength to 0
    strength = 0
    #ask if the user wants to quit 
    check = input("Do you want to quit? If so, please write \"q\". If not, feel free to write anything. ")
    #if they want to quit
    if check == "q":
        #end the loop
        break
    #Ask the user for the password
    password = input("Please write your prospective password. ").strip()
    #if it is longer than 7 letters
    if len(password) > 7:
        #add 1 to the password strength
        strength += 1
    #otherwise
    else:
        #say that they need to make their password longer
        print("You could make your password longer. ")
    #looping through every single letter
    for letter in password:
        #check if that letter is uppercase
        if letter.isupper():
            #add 1 to the password strength
            strength += 1
            break
        #otherwise
        else:
            #say that they have to add an uppercase letter
            print("You should add an uppercase letter. ")
    #looping through every single letter
    for letter in password:
        #check if that letter is lowercase
        if letter.islower():
            #add 1 to the password strength
            strength += 1
        #otherwise
        else:
            #say that they have to add an lowercase letter
            print("You should add a lowercase letter. ")
    #check if the string is not alpha numeric (isalnum)
    if password not.isalnum:
        #add 1 to the password strength
        strength += 1
    #otherwise
    else:
        #say that they need to add a special character
        print("You should add a special character. ")
    #looping through every single letter
    for letter in password:
        #check if that letter is numeric
        if letter.isnum():
            #add 1 to the password strength
            strength += 1
        #otherwise
        else:
            #say that they have to add an number
            print("You should add a number. ")
    #display the password strength
    print(f"Your password strength is {strength}. ")
