#BHR 2nd conditional notes
import random
enemies = []
while True:
    player_hp = input("What is your health? ")
    if player_hp.isnumeric():
        player_hp = int(player_hp)
        if player_hp > 0:
            break
        else:
            print("That is invalid. Please try again. ")
    else:
        print("That is invalid. Please try again. ")
while True:
    armor_class = input("What is your armor class? ")
    if armor_class.isnumeric():
        armor_class = int(armor_class)
        if armor_class > 0:
            break
        else:
            print("That is invalid. Please try again. ")
    else:
        print("That is invalid. Please try again. ")
while True:
    dmg_modifier = input("What is your damage modifier? ")
    if dmg_modifier.isnumeric():
        dmg_modifier = int(dmg_modifier)
        if  dmg_modifier > -0.01:
            break
        else:
            print("That is invalid. Please try again. ")
    else:
        print("That is invalid. Please try again. ")
while True:
    attack_bonus = input("What is your attack bonus? ")
    if attack_bonus.isnumeric():
        attack_bonus = int(attack_bonus)
        if attack_bonus > -0.01:
            break
        else:
            print("That is invalid. Please try again. ")
    else:
        print("That is invalid. Please try again. ")

amount_of_monster = int(input("How many enemies are there? "))
enemies.append(amount_of_monster)
amount = amount_of_monster
monster_health = []
monster_ac = []
monster_damage_modifier = []
names = []
while amount >= 0:
    while True:
        name = input("What is the name of this enemy? ")
        if name in names or name.isnumeric():
            print("That name is invalid. Please try again. ")
        else:
            break
    while True:
        monster_hp = input("What is the enemy's hp? ")
        if monster_hp.isnumeric():
            monster_hp = int(monster_hp)
            if monster_hp > 0:
                monster_health.append(monster_hp)
                break
            else:
                print("That is invalid. Please try again. ")
        else:
            print("That is invalid. Please try again. ")
    while True:
        monster_armor_class = input("What is the enemy's armor class? ")
        if monster_armor_class.isnumeric():
            monster_armor_class = int(monster_armor_class)
            if monster_armor_class > -0.01:
                monster_ac.append(monster_armor_class)
                break
            else:
                print("That is invalid. Please try again. ")
        else:
            print("That is invalid. Please try again. ")
    while True:
        monster_dmg_modifier = input("What is the enemy's damage modifier? ")
        if monster_dmg_modifier.isnumeric():
            monster_dmg_modifier = int(monster_dmg_modifier)
            if monster_dmg_modifier > -0.01:
                monster_damage_modifier.append(monster_dmg_modifier)
                break
            else:
                print("That is invalid. Please try again. ")
        else:
            print("That is invalid. Please try again. ")
    amount -= 1

while monster_hp >= 0:
    roll = (random.randint(1,20) + attack_bonus)
    monster_roll =  random.randint(1,20)
    #while True:
     #   monster = input("Which enemy are you attacking? (Please write the full name)")
      #  if monster in names:
       #     monster = 
        #    break
    while True:
        dice = input("What is the dice you are using? ")
        if dice.isnumeric():
            dice = int(dice)
            if dice > 0:
                break
            else:
                print("That is invalid. Please try again. ")
        else:
            print("That is invalid. Please try again. ")
    if roll > monster_armor_class:
        if roll == 20:
            print("You rolled a critical! Double your damage.")
            attack = random.randint(1,dice) + random.randint(1,dice) + dmg_modifier
            monster_hp -= attack
            if monster_hp <= 0:
                print(f"The monster took {attack} damage. It's health is now 0")
            else:
                print(f"The monster took {attack} damage. It's health is now {monster_hp}")
        else:
            print("You hit!")
            attack = random.randint(1,dice) + dmg_modifier
            monster_hp -= attack
            if monster_hp <= 0:
                print(f"The monster took {attack} damage. It's health is now 0")
            else:
                print(f"The monster took {attack} damage. It's health is now {monster_hp}")
    elif roll <= monster_armor_class:
        if roll <= 1:
            damage = (random.randint(1,random.randint(1,10)) + monster_dmg_modifier)
            player_hp -= damage
            if player_hp <= 0:
                print(f"You took {attack} damage. You now have 0 health. ")
            else:
                print(f"You took {damage} damage. You now have {player_hp}")
        else:
            print("You missed!")
    else:
        print("That is weird. You did something wrong. ")
    if monster_hp <= 0:
        print(f"The monster's health is now 0")
        break
    print("Your turn is over. ")
    for name in names:
        monster_dice = input(f"What is the dice the {name} is using? ")
        if monster_dice.isnumeric():
            monster_dice = int(monster_dice)
            if monster_dice > 0:
                break
            else:
                print("That is invalid. Please try again. ")
        else:
            print("That is invalid. Please try again. ")
    if monster_roll > armor_class:
        if monster_roll == 20:
            print(f"The {name} rolled a critical! Their damage is doubled.")
            damage = random.randint(1,monster_dice) + random.randint(1,monster_dice) + monster_dmg_modifier
            player_hp -= damage
            if player_hp <= 0:
                print(f"You took {attack} damage. You now have 0 health. ")
            else:
                print(f"You took {damage} damage. You now have {player_hp}")
        else:
            print(f"The {name} hit!")
            damage = random.randint(1,monster_dice) + monster_dmg_modifier
            player_hp -= damage
            if player_hp <= 0:
                print(f"You took {attack} damage. You now have 0 health. ")
            else:
                print(f"You took {damage} damage. You now have {player_hp}")
    elif monster_roll <= armor_class:
        if monster_roll <=1:
            attack = (random.randint(1,random.randint(1,10)) + dmg_modifier)
            monster_hp -= attack
            if monster_hp <= 0:
                print(f"The {name} took {attack} damage. It's health is now 0")
            else:
                print(f"The {name} took {attack} damage. It's health is now {monster_hp}")
        print(f"The {name} missed!")
    else:
        print("That is weird. You did something wrong. ")
    if player_hp <= 0:
        print(f"Your health is now 0. You lost")
        break
    print(f"The {name}'s turn is over. ")
print("Your turn is over. ")
