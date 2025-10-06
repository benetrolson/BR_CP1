# BHR 2nd Rock Paper Scissors

import random
import time
score = 0
robo_score = 0
print("Welcome to rock paper scissors. ")
while True:
    choose = 0
    print(f"Your score is :{score}")
    print(f"The robot's score is :{robo_score}")
    choice = input("Which do you want to choose, rock(r), paper(p), or scissors(s)? If you want to quit, then write 'q'. ")
    if choice == "q":
        break
    elif choice == "r":
        choose = 1
    elif choice == "p":
        choose = 2
    elif choice == "s":
        choose = 3
    robot_choice = random.randint(1,3)

    if choose == 1 and robot_choice == 3:
        print("You won! ")
        print("""You chose rock!    
            ______________                                                                                                                                                               
 ........../      _______) 
                  (_______)
                  (_______)
                  (_______)
-------,__________(_____)
""")
        print("""The robot chose scissors!
            _____________                                                                                                                                                               
 ........../          ___)_________
                      _____________)
                     ____________)
                  (______)     
-------,__________(_____)
""")
        score += 1
    elif choose == 2 and robot_choice == 1:
        print("You won! ")
        print("""You chose paper!
            _____________                                                                                                                                                               
 ........../          ___)__
                      ______)
                     _______)
                  ________)
-------,_______________)
""")
        print("""The robot chose rock!    
            ______________                                                                                                                                                               
 ........../      _______) 
                  (_______)
                  (_______)
                  (_______)
-------,__________(_____)
""")
        score += 1
    elif choose == 3 and robot_choice == 2:
        print("You won! ")
        print("""You chose scissors!
            _____________                                                                                                                                                               
 ........../          ___)_________
                      _____________)
                     ____________)
                  (______)     
-------,__________(_____)
""")
        print("""The robot chose paper!
            _____________                                                                                                                                                               
 ........../          ___)__
                      ______)
                     _______)
                  ________)
-------,_______________)
""")
        score += 1
    elif choose == 1 and robot_choice == 1:
        print("You tied! ")
        print("""You chose rock!    
            ______________                                                                                                                                                               
 ........../      _______) 
                  (_______)
                  (_______)
                  (_______)
-------,__________(_____)
""")
        print("""The robot chose rock!    
            ______________                                                                                                                                                               
 ........../      _______) 
                  (_______)
                  (_______)
                  (_______)
-------,__________(_____)
""")
    elif choose == 2 and robot_choice == 2:
        print("You tied! ")
        print("""You chose paper!
            _____________                                                                                                                                                               
 ........../          ___)__
                      ______)
                     _______)
                  ________)
-------,_______________)
""")
        print("""The robot chose paper!
            _____________                                                                                                                                                               
 ........../          ___)__
                      ______)
                     _______)
                  ________)
-------,_______________)
""")
    elif choose == 3 and robot_choice == 3:
        print("You tied! ")
        print("""You chose scissors!
            _____________                                                                                                                                                               
 ........../          ___)_________
                      _____________)
                     ____________)
                  (______)     
-------,__________(_____)
""")
        print("""The robot chose scissors!
            _____________                                                                                                                                                               
 ........../          ___)_________
                      _____________)
                     ____________)
                  (______)     
-------,__________(_____)
""")
    elif choose == 1 and robot_choice == 2:
        print("You lost!")
        print("""You chose rock!    
            ______________                                                                                                                                                               
 ........../      _______) 
                  (_______)
                  (_______)
                  (_______)
-------,__________(_____)
""")
        print("""The robot chose paper!
            _____________                                                                                                                                                               
 ........../          ___)__
                      ______)
                     _______)
                  ________)
-------,_______________)
""")
        robo_score += 1
    elif choose == 2 and robot_choice == 3:
        print("You lost!")
        print("""You chose paper!
            _____________                                                                                                                                                               
 ........../          ___)__
                      ______)
                     _______)
                  ________)
-------,_______________)
""")
        print("""The robot chose scissors!
            _____________                                                                                                                                                               
 ........../          ___)_________
                      _____________)
                     ____________)
                  (______)     
-------,__________(_____)
""")
        robo_score += 1
    elif choose == 3 and robot_choice == 1:
        print("You lost!")
        print("""You chose scissors!
            _____________                                                                                                                                                               
 ........../          ___)_________
                      _____________)
                     ____________)
                  (______)     
-------,__________(_____)
""")
        print("""The robot chose rock!    
            ______________                                                                                                                                                               
 ........../      _______) 
                  (_______)
                  (_______)
                  (_______)
-------,__________(_____)
""")
        robo_score += 1
    else:
        print("How dare you do such a thing. You shall pay for writing something wrong! ")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        robo_score += 5
        score -= 10
        secret = input("You have paid for your actions now you will never get to beat me EVER again! mwahahahahahahahha ")
        if secret == "Bennett is the best":
            score += 60
        
