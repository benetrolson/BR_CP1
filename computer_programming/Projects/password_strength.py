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
    if password > 7:
        #add 1 to the password strength
        strength += 1
    #otherwise

        #say that they need to make their password longer

    #looping through every single letter

        #check if that letter is uppercase

            #add 1 to the password strength
            
        #otherwise

            #say that they have to add an uppercase letter

    #looping through every single letter

        #check if that letter is lowercase

            #add 1 to the password strength

        #otherwise

            #say that they have to add an lowercase letter

    #check if the string is not alpha numeric (isalnum)

        #add 1 to the password strength

    #otherwise

        #say that they need to add a special character

    #looping through every single letter

        #check if that letter is numeric

            #add 1 to the password strength

        #otherwise

            #say that they have to add an number

    #display the password strength


