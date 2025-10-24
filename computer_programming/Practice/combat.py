#BHR 2nd combat program
import random
def attack(stats):
    stats += 1


while True:
    name = input("What is your name? ")
    bird = input("Which bird are you? chicken(1), pigeon(2), duck(3)")
    if bird == "1":
        player_stats = [50, 4, 10, 10, 3, 2]#order is health, defense, attack, damage, attack modifier, damage modifier
    elif bird == "2":
        player_stats = [25, 2, 20, 20, 4, 5]
    elif bird == "3":
        player_stats = [100, 8, 5, 5, 2, 1]
    else:
        continue
    turn = random.randint(1,2)
    enemy = random.randint(1,3)
    if enemy == 1:
        enemy_stats = [50, 4, 10, 10, 3, 2]#order is health, defense, attack, damage, attack modifier, damage modifier
    elif enemy == 2:
        enemy_stats = [25, 2, 20, 20, 4, 5]
    elif enemy == 3:
        enemy_stats = [100, 8, 5, 5, 2, 1]
    while enemy_stats[1] > 0 and player_stats[1] > 0:
        print(f"Your stats are health:{player_stats[0]}, defense:{player_stats[1]}, attack:{player_stats[2]} + {player_stats[4]}, damage:{player_stats[3]} + {player_stats[5]}. ")
        print(f"Your enemy's stats are health:{enemy_stats[0]}, defense:{enemy_stats[1]}, attack:{enemy_stats[2]} + {enemy_stats[4]}, damage:{enemy_stats[3]} + {enemy_stats[5]}. ")
        if turn == 1:
            print(f"The enemy did")
            turn += 1
