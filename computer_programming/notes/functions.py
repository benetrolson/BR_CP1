# BHR 2nd Functions Notes
#all imports
#set global variables
num = 0
player_hp = 100
monster_hp = 100

#write your functions
def add(x,y):
    return x+y

while num < add(5,5):
    print("Duck")
    num+=1

def initials(name):
    names = name.split(" ")
    initial = []
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg

print("Goose")
print(f"Results is: {add(-6519146,36516)}")
total = add(-6519146,36516)
add(689461,654894)
add(3.14,.85)
add(42,7)

print(f"Tia's initials are: {initials("Tia LaRose")}")
print(f"Xavier's initials are: {initials("Xavier LaRose")}")
monster_hp, player_hp = attack(15, "monster")
print(f"Player health: {player_hp}")
print(f"Monster health: {monster_hp}")
monster_hp, player_hp = attack(15, "player")
print(f"Player health: {player_hp}")
print(f"Monster health: {monster_hp}")
