#BHR 2nd conditional notes
import random
monster_hp = 30
dmg_modifier = 2
atack_bonus = 3
player_hp = 25

while monster_hp >= 0:
    roll = random.randint(1,20)
    monster_roll =  random.randint(1,20)
    if roll == 20:
        print("You rolled a critical! Double your damage.")
        attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
        monster_hp -= attack
        print(f"The monster took {attack} damage. It's health is now {monster_hp}")
    if roll > 10:
        print("You hit!")
        attack = random.randint(1,8) + dmg_modifier
        monster_hp -= attack
        print(f"The monster took {attack} damage. It's health is now {monster_hp}")
    elif roll <= 10:
        if roll <= 1:
            damage = (random.randint(1,10) + 2)
            player_hp -= damage
            print(f"You took {damage} damage. You now have {player_hp}")
        else:
            print("You missed!")
    else:
        print("That is weird. You did something wrong. ")
    if monster_hp <= 0:
        print(f"The monster's health is now 0")
        break
    print("Your turn is over. ")
    if monster_roll == 20:
        print("The monster rolled a critical! Their damage is doubled.")
        damage = random.randint(1,8) + random.randint(1,8) + dmg_modifier
        player_hp -= damage
        print(f"Your health is now {player_hp}")
    if monster_roll > 10:
        print("The monster hit!")
        damage = random.randint(1,8) + dmg_modifier
        player_hp -= damage
        print(f"Your health is now {player_hp}")
    elif monster_roll <= 10:
        if monster_roll <=1:
            attack = (random.randint(1,10) + 2)
            print(f"The monster took {attack} damage. It's health is now {monster_hp}")
        print("The monster missed!")
    else:
        print("That is weird. You did something wrong. ")
    if player_hp <= 0:
        print(f"Your health is now 0. You lost")
        break
    print("The monster's turn is over. ")
print("Your turn is over. ")
