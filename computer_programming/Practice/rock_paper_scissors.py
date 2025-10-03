# BHR 2nd Rock Paper Scissors

import random

print("Welcome to rock paper scissors. ")
while True:
    choice = input("Which do you want to choose, rock(r), paper(p), or scissors(s)? If you want to quit, then write 'q'. ")
    if choice == "w":
        break
    elif choice == "r":
        choose = 1
    elif choice == "p":
        choose = 2
    elif choice == "s":
        choose = 3

