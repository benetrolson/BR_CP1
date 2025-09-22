#BHR 2nd user sign in
user1 = "George"
pass1 = "hardPassword"
user2 = "Ms. LaRose"
pass2 = "superStrongPassword"
user3 = "Bob"
pass3 = "secretPassword"
user4 = "Gregory"
pass4 = "difficultPassword"
user5 = "Gregorius"
pass5 = "impossiblePassword"
user6 = "Harold"
pass6 = "passw0rd"

while True:
    trying_user = input("What is your username? ")
    trying_pass = input("What is your password? ")
    if trying_user == user1 and trying_pass == pass1:
        print("Welcome George. ")
        break
    elif trying_user == user2 and trying_pass == pass2:
        print("Welcome Ms. LaRose. ")
        break
    elif trying_user == user3 and trying_pass == pass3:
        print("Welcome Bob. ")
        break
    elif trying_user == user4 and trying_pass == pass4:
        print("Welcome Gregory. ")
        break
    elif trying_user == user5 and trying_pass == pass5:
        print("Welcome Gregorius. ")
        break
    elif trying_user == user6 and trying_pass == pass6:
        print("Welcome Harold. ")
        break
    else:
        print("You have an invalid username or password. Please try again. ")



