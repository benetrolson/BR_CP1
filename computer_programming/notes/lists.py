#BHR 2nd lists notes
import random

names = ["Alex", "Katie", "Cora", "Andrew", "Jake", "Eric", 5, 3.14, False]

print(names)
print(names[3])
print(names[random.randint(1,len(names))])
print(random.choice(names))
names[-1] = names
names.extend(["Trayson", "Tia"])
names += ["Joseph", "Israel", "Zee"]
names.remove(3.14)
names.insert(3, "Vienna")
number = names.index(5)
names.pop(number)
print(names)

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

board[1][1] = "X"

print(board)
#List (changable, ordered)
#Tuple (not changable, ordered)
classes = ("Bard", "Monk", "Barbarian", "Paladin")
#Set (changeable, unordered)
fruit = {"Apple", "Orange", "Strawberry", "Kiwi"}
print(fruit)
