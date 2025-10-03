# BHR 2nd Rock Paper Scissors

import random

print("Welcome to rock paper scissors. ")
while True:
    choice = input("Which do you want to choose, rock(r), paper(p), or scissors(s)? If you want to quit, then write 'q'. ")
    if choice == "q":
        break
    elif choice == "r":
        choose = 1
    elif choice == "p":
        choose = 2
    elif choice == "s":
        choose = 3
robo_choice = random.randint(1,3)

if choose == 1 and robot_choice == 2 or choose == 2 and robot_choice == 3 or choose == 3 and robot_choice == 1:
    print("You won! ")
elif choose == 1 and robot_choice == 1 or choose == 2 and robot_choice == 2 or choose == 3 and robot_choice == 3:
