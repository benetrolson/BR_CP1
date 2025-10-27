#BHR 2nd combat program
import random
import time
def attack(action, attacking_stats, defending_stats):
    if action == 1:
        damage = int(random.randint(1, attacking_stats[2]) + attacking_stats[3]) - int(random.randint(1, defending_stats[1]))
        hurt = 0
    elif action == 2:
        damage = int(random.randint(1, attacking_stats[2]) * 1.5 + attacking_stats[3]) - int(random.randint(1, defending_stats[1]))
        hurt = int(damage/3)
    elif action == 3:
        damage = int(random.randint(1, attacking_stats[2]) * 0.75 + attacking_stats[3]) - int(random.randint(1, defending_stats[1]))
        hurt = int(-damage/1.5)#healing
    elif action == 4:
        damage = int(random.randint(1, attacking_stats[2]) * 2 + attacking_stats[3]) - int(random.randint(1, defending_stats[1]))
        hurt = int(damage/2)
    else:
        damage = ("error")
        hurt = ("error")
    if damage < 0:
        damage = 0
    return(damage, hurt)


while True:
    bird = input("Which bird are you? chicken(1), pigeon(2), duck(3)")
    if bird == "1":
        player_stats = [50, 4, 10, 3]#order is health, defense, attack, damage, attack modifier, damage modifier
    elif bird == "2":
        player_stats = [25, 3, 20, 6]
    elif bird == "3":
        player_stats = [75, 6, 5, 2]
    else:
        print("That is an invalid input. ")
        continue
    turn = random.randint(1,2)
    enemy = random.randint(1,3)
    if enemy == 1:
        enemy_stats = [50, 4, 10, 3]#order is health, defense, attack, attack modifier
        enemy = "chicken"
    elif enemy == 2:
        enemy_stats = [25, 3, 20, 6]
        enemy = "pigeon"
    elif enemy == 3:
        enemy_stats = [75, 6, 5, 2]
        enemy = "duck"
    print(f"You have been ambushed by a {enemy}! Prepare for combat. ")
    time.sleep(0.3)
    check = input("Do you want to have a guide to what each attack does? If so, write yes. If not, write anything. ")
    time.sleep(0.3)
    if check == "yes":
        print("To peck is to do basic damage without wounding oneself. \nTo claw is to do more damage but to do some damage to oneself. \nTo fly is to do weak damage but heal oneself. \nTo dive is to do a lot of damage but to do a lot of damage to oneself. ")
    while enemy_stats[0] > 0 and player_stats[0] > 0:
        print(f"Your stats are health:{player_stats[0]}, defense:{player_stats[1]}, attack:{player_stats[2]} + {player_stats[3]}. ")
        time.sleep(0.3)
        print(f"Your enemy's stats are health:{enemy_stats[0]}, defense:{enemy_stats[1]}, attack:{enemy_stats[2]} + {enemy_stats[3]}. ")
        time.sleep(0.3)
        if turn == 1:
            while True:
                action = input(f"It is your turn. What action do you want to do? Peck(1), claw(2), fly(3), dive(4)")
                if action != "1" and action != "2" and action != "3" and action != "4":
                    print("That is an invalid input. ")
                else:
                    action = int(action)
                    break
            turn += 1
            damage, hurt = attack(action, player_stats, enemy_stats)
            time.sleep(0.3)
            wait = input(f"You did {damage} damage to your enemy. You did {hurt} damage to yourself. ")
            enemy_stats[0] -= damage
            player_stats[0] -= hurt
        elif turn == 2:
            action = random.randint(1,4)
            turn -= 1
            damage, hurt = attack(action, enemy_stats, player_stats)
            time.sleep(0.3)
            wait = input(f"The enemy did {damage} damage to you. They did {hurt} damage to themself. ")
            time.sleep(0.3)
            player_stats[0] -= damage
            enemy_stats[0] -= hurt
    if player_stats[0] <= 0:
        print("You lost. Good job. ")
        time.sleep(0.3)
    elif enemy_stats[0] <= 0:
        print("How did you win!?! Good job! ")
        time.sleep(0.3)
    else:
        print("Why did you have to break the game? ")
        time.sleep(0.3)
