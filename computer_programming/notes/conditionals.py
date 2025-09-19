#BHR 2nd conditional notes
import random
monster_hp = 30
dmg_modifier = 2
atack_bonus = 3
player_hp = 25

roll = random.randint(1,20)
monster_roll =  random.randint(1,20)
while monster_hp >= 0:
    if roll == 20:
        print("You rolled a critical! Double your damage.")
        attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
        monster_hp -= attack
    if roll > 10:
        print("You hit!")
        attack = random.randint(1,8) + dmg_modifier
        monster_hp -= attack
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
    else:
        print(f"The monster's health is now {monster_hp}")
    print("Your turn is over. ")
    if monster_roll == 20:
        print("The monster rolled a critical! Their damage is doubled.")
        attack = random.randint(1,8) + random.randint(1,8) + dmg_modifier
        player_hp -= attack
    if monster_roll > 10:
        print("You hit!")
        attack = random.randint(1,8) + dmg_modifier
        player_hp -= attack
    elif monster_roll <= 10:
        print("You missed!")
    else:
        print("That is weird. You did something wrong. ")
    if player_hp <= 0:
        print(f"Your health is now 0")
        break
    else:
        print(f"Your health is now {player_hp}")
    print("Your turn is over. ")
print("Your turn is over. ")

