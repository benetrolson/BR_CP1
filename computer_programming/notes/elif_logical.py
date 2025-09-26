#BHR 2nd Elif and logical operators notes

homework = True
chores = False
room = False

if homework and chores and room:
    print("You can go to your friends house. ")
elif not chores or not room:
    print("GO DO YOUR CHORES! ")
else:
    print("FINISH YOUR HOMEWORK RIGHT NOW! ")

username = input("Enter your username: ")
password = input("Enter you password: ")

if username == "MaLaRose":
    if password == "1234":
        print("Welcome Ms. LaRose")
    else:
        print("Incorrect password. ")
elif username == "Tia" and password == "password":
    pass
elif username == "Andrew" and password == "orange":
    print("Welcome Andrew. ")
else:
    print("Welcome hacker. ")
    