import random
board = []
while True:
    robo_choice = random.randint(1,10)
    if robo_choice in board:
        robo_check = board.index(robo_choice)
        board(robo_check) = "X"
        break

print(f"""
  {board(1)} | {board(2)} | {board(3)}

  {board(1)} | {board(2)} | {board(3)}

""")
while True:
    choice = int(input("Which square do you want to choose? "))
    if choice in board:
        check = board.index(choice)
        board(check) = "O"
        break
    print("That is an invalid choice. ")

