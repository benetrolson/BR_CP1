# Final Project

# Import the random functions
import random
check = "yes"
enemy = None
necklaces = ["intelligence", "strength", "health"]
# Set the player stats in a definition:
player_stats = {
        # Stats:
        "stats": {
                # Intelligence: 50
                "intelligence": 50,
                # Strength: 50
                "strength": 50,
                # Health: 50
                "max_health": 50
        },
        "current_health": 50,
        # Weapons: List of all the weapons that the player has
        "weapons": {
                # Equipped:
                "equipped": {
                        "sword": {"cooldown": 0},
                },
                "unequipped": [],
        },
        # Health potions: 0
        "health_potions": 0,
        # Necklace: whichever necklace they have equipped
        "necklace": "",
        # Location: Beginning
        "location": "beginning"
}

# Set the enemy stats in a definition:
enemies = {
        # Kid’s stats:
        "kid": {
                # 1 weapon can either be sword, axe, spear, or club
                # Health is 20
                "health": 20,
                # Strength is 20
                "strength": 20
        },

        # Adult’s stats:
        "adult": {
                # 2 weapons can either be sword, axe, spear, or club
                # Health is 40
                "health": 40,
                # Strength is 40
                "strength": 40
        },

        # Old’s stats:
        "old": {
                # 3 weapons can either be sword, axe, spear, or club
                # Health is 20
                "health": 20,
                # Strength is 50
                "strength": 50
        },

        # Gatekeeper’s stats:
        "gatekeeper": {
                # Weapon is axe, club, beak
                # Health is 50
                "health": 50,
                # Strength is 50
                "strength": 50
        },

        # Boss’s stats:
        "boss": {
                # Weapon is axe, club, sword, spear
                # Health is 60
                "health": 60,
                # Strength is 60
                "strength": 60
        }
}

# Set the weapon stats in a definition (for example):
weapons = {
        # Beak
        "beak": {
                # Damage is 1
                "dmg": 1,
                # Cooldown is 0
                "cooldown": 0
        },

        # Sword:
        "sword": {
                # Damage is 5
                "dmg": 5,
                # Cooldown is 2
                "cooldown": 2
        },

        # Axe:
        "axe": {
                # Damage is 6
                "dmg": 6,
                # Cooldown is 4
                "cooldown": 4
        },

        # Spear:
        "spear": {
                # Damage is 3
                "dmg": 3,
                # Cooldown is 1
                "cooldown": 1
        },

        # Club:
        "club": {
                # Damage is 4
                "dmg": 4,
                # Cooldown is 3
                "cooldown": 3
        },

        # Health potion:
        "health_potions": {
                # Heals 10 health
                "heal": 10,
                # Cooldown is 0
                "cooldown": 0
        },

        # Health necklace:
        "health necklace": {
                # Adds 20 health
                "health": 20
        },

        # Strength necklace:
        "strength necklace": {
                # Adds 20 strength
                "strength": 20
        },

        # Intelligence necklace:
        "intelligence necklace": {
                # Adds 20 intelligence
                "intelligence": 20
        },

        # Super necklace:
        "super necklace": {
                # Adds 20 health
                "health": 20,
                # Adds 20 strength
                "strength": 20,
                # Adds 20 intelligence
                "intelligence": 20
        }
}

# Set the rooms in a definition:
rooms = {
        # Beginning:
        "beginning": {
                # Possible places to move to: bob, bonus area 1, tutorial
                "possibilities": ["bob", "bonus area 1", "tutorial"],
                # Sword has been taken
                "sword": "",
                # Description:
                "description 1": "You return to the place where you woke up. You look around, remembering that the omnipotent and omniscient chickens have sent you down with a purpose, to destroy Earth. ",
                "visited": True
        },
        # Tutorial:
        "tutorial": {
                # Possible places to move to: beginning, bob, gladiator ring, shop
                "possibilities": ["beginning", "bob", "gladiator ring", "shop"],
                # Kid has not been killed
                "kid": True,
                # Description 1:
                "description 1": "You enter a room with a kid in the center. The kid runs up at you and starts attacking you. Prepare for combat. ",
                # Description 2:
                "description 2": "You enter a room with a dead kid in the center. You see the spilled blood on the floor. The walls are covered in a beautiful mosaic of Bob. ",
                "visited": False
        },
        # Bob:
        "bob": {
                # Possible places to move to
                "possibilities": ["beginning", "tutorial", "boss room"],
                # Intelligence necklace has been taken
                "necklaces": {
                        "intelligence": "",
                        # Health necklace has not been taken
                        "health": "",
                        # Strength necklace has not been taken
                        "strength": ""
                },
                # Description 1:
                "description 1": "A chicken sits there, fingering his sword. He waits for you to approach him, holding some necklaces. ",
                # Description 2:
                "description 2": "Bob sits there, waiting for you to approach him. It seems he wishes for you to stay away from that room with arcane energy pulsing through. ",
                "visited": False
        },
        # Gladiator Ring:
        "gladiator ring": {
                "possibilities": ["tutorial", "shop", "mage", "bonus area 1", "bonus area 2"],
                "order of fights": {
                        1: ["kid"],
                        2: ["kid", "kid"],
                        3: ["adult"],
                        4: ["kid", "adult"],
                        5: ["adult", "adult"],
                        "bonus area 1": "",
                        6: ["kid", "old"],
                        7: ["adult", "old"],
                        8: ["old", "old"],
                        9: ["adult", "adult", "adult"],
                        10: ["old", "old", "old"],
                        "bonus area 2": ""
                },
                "description 1": "A chicken with a boisterous voice welcomes you to his arena, seeking entertainment. He decides to have you battle some of his slaves to give him entertainment. ",
                "description 2": "The man asks you whether you want to fight another family member or leave. ",
                "visited": False
        },
        # Shop:
        "shop": {
                "possibilities": ["bob", "tutorial", "gladiator ring", "mage"],
                "description 1": "You find a strange chicken with a bunch of weapons. The chicken seems to wish for something. She awaits your approach. ",
                "visited": False
        },
        # Mage:
        "mage": {
                "possibilities": ["gladiator ring", "shop", "gatekeeper"],
                "boost": "",
                "description 1": "A floating chicken stands in the center of the room, walking around. They turn to face you while they stay still, watching you. ",
                "description 2": "The mage waits while floating at the top of the room, running along the ground, at the center of the edge of the center of the room. ",
                "visited": False
        },
        # Gatekeeper:
        "gatekeeper": {
                "possibilities": ["shop", "mage", "resting place"],
                "gatekeeper": True,
                "description 1": "A chicken, seeming to be using arcane energy from the room ahead, floats up and flies towards you. ",
                "description 2": "The gatekeeper lies on the ground, dead. ",
                "visited": False
        },
        # Resting place:
        "resting place": {
                "possibilities": ["gatekeeper", "boss room"],
                "health potion": True,
                "description 1": "You see a health potion on the ground, and only one way to go; forward. ",
                "description 2": "You see the way that you should go: forward. ",
                "visited": False
        },
        # Boss room:
        "boss room": {
                "possibilities": ["bob", "gatekeeper"],
                "description 1": "A door slams behind you, locking you into the room. The Chickens look at you, seeming prepared. One speaks, saying, “We may not be omniscient, but we are omnipotent. If you survive the final trial, Us, while we don’t really try, you may ascend up and join us in our pursuit of omniscience.”",
                "visited": False
        },
        # Bonus area 1:
        "bonus area 1": {
                "possibilities": ["gladiator ring"],
                "intelligence necklace": "",
                "health necklace": "",
                "strength necklace": "",
                "description 1": "You see the great and glorious Bob again, waiting with his necklaces. ",
                "description 2": "Bob, bored, asks why you are here and to shut the nonexistent door on the way out. ",
                "visited": False
        },
        # Bonus area 2:
        "bonus area 2": {
                "possibilities": ["gladiator ring", "beginning"],
                "description 1": "Bob welcomes you, and gives you a weird necklace after taking yours. He then says “Out! My life’s goal is complete: To eat a necklace worn by a chicken! Now I have two to eat! ”",
                "description 2": "Bob greets you with a cheerful “SHUT THE (nonexistent) DOOR ON YOUR WAY OUT!”",
                "visited": False
        },
}

dialogue = {
        "bob": ["Welcome in! I hope you have a good day. ", "I'll see you tomorrow, if you d leave me. ", "Fine. "],
        "mage": ["Hello good sir! ", "Are you looking for a boost in you magical ability? "],
        "shop": ["Welcome, welcome. ", "I exchange weapons for health potions. ", "Do you want some? "],
        "gladiator ring": ["Welcome to my arena! ", "Care to fight my slaves, I mean soldiers? "],
        "bonus area 1": ["You again? "],
        "bonus area 2": ["WELCOME BACK! "]
}

# Set the combat as a function and the parameters as: enemy, info about all enemies, player health, player strength, the list of equipped items, the weapon(s) the enemy has, the enemy’s health, whose turn it is, which weapon the player wants to attack with:
def combat(enemy, turn, weapon, enemies=enemies, player_stats=player_stats):
        possibilities = []
        # If the enemy is attacking:
        if turn == 0:
                # See how many available weapons the enemy has and store that in a variable
                usable_weapons = [i for i, w in enumerate(enemy["weapon"]) if w["cooldown"] == 0]
                # If they have some:
                if usable_weapons:
                        # Infinite loop:
                        # Pick a random number between 0 and len(usable_weapons)-1
                        weapon_choice = random.choice(usable_weapons)
                        weapon_dict = enemy["weapon"][weapon_choice]
                        weapon_name = weapon_dict["name"]
                        # If that corresponds with an available weapon:
                        # Calculate the damage as ((strength / 100) + 1) * dmg_of_weapon
                        damage = ((enemy["strength"] / 100) + 1) * weapons[weapon_name]["dmg"]
                        # Drop each cooldown drop by one
                        for w in enemy["weapon"]:
                                if w["cooldown"] > 0:
                                        w["cooldown"] -= 1
                        # Set the weapon that you just used to their respective cooldown
                        enemy["weapon"][weapon_choice]["cooldown"] = weapons[weapon_name]["cooldown"]
                        # Return the damage
                        return damage, enemy, player_stats
                else:
                        # No weapons are usable: do a default attack (e.g., minimal damage)
                        for w in enemy["weapon"]:
                                if w["cooldown"] > 0:
                                        w["cooldown"] -= 1
                        return 1, enemy, player_stats  # default weak attack
        # Otherwise if the player is attacking:
        elif turn == 1:
        # If the player didn’t input a weapon yet
                if weapon == "":
                        # If the player has no possible weapons
                        for w in player_stats["weapons"]["equipped"]:
                                if player_stats["weapons"]["equipped"][w]["cooldown"] == 0:
                                        possibilities.append(w)
                        # Return by give them one option; to attack with the beak
                        if possibilities == []:
                                return ["beak"], enemy, player_stats
                        else:
                                return possibilities, enemy, player_stats
        # If the player chose a weapon they have and it’s ready
        elif weapon in player_stats["weapons"]["equipped"] and player_stats["weapons"]["equipped"][weapon]["cooldown"] == 0:
                # Calculate the damage as ((strength / 100) + 1) * dmg_of_weapon
                damage = ((player_stats["stats"]["strength"] / 100) + 1) * weapons[weapon]["dmg"]
                # If any cooldowns are bigger than 0:
                for w in player_stats["weapons"]["equipped"]:
                        if player_stats["weapons"]["equipped"][w]["cooldown"] > 0:
                                player_stats["weapons"]["equipped"][w]["cooldown"] -= 1
                # Set the cooldown to its respective time
                player_stats["weapons"]["equipped"][weapon]["cooldown"] = weapons[weapon]["cooldown"]
                # Return the damage
                return damage, enemy, player_stats
        # Otherwise if they inputted a health potion:
        elif weapon == "health_potions" and player_stats["health_potions"] > 0:
                if player_stats["current_health"] + 10 >= player_stats["stats"]["max_health"]:
                        player_stats["current_health"] = player_stats["stats"]["max_health"]
                else:
                        # Add 10 health to the player’s health
                        player_stats["current_health"] += 10
                player_stats["health_potions"] -= 1
                # If any cooldowns are bigger than 0:
                for w in player_stats["weapons"]["equipped"]:
                        if player_stats["weapons"]["equipped"][w]["cooldown"] > 0:
                                player_stats["weapons"]["equipped"][w]["cooldown"] -= 1
                # Return that
                return "healed", enemy, player_stats
        # Otherwise:
        # Loop 4 times:
        usable_options = []
        for w in list(player_stats["weapons"]["equipped"])[:4]:
                # If the weapon is usable:
                if player_stats["weapons"]["equipped"][w]["cooldown"] == 0:
                        # Add it to a list
                        usable_options.append(w)
        # If the player has health potions:
        if player_stats["health_potions"] > 0:
                # Add it to the list
                usable_options.append("health_potions")
        # Return the list
        return usable_options, enemy, player_stats

def move(options, rooms = rooms, player_stats = player_stats):
        if options == "":
                return(rooms[player_stats["location"]]["possibilities"])
        else:
                player_stats["location"] = options
                return(player_stats)

def loot_enemy(enemy, player_stats):
        dropped_weapons = [w["name"] for w in enemy.get("weapon", [])]
        for w in dropped_weapons:
                # Equip if there is a free slot (max 4 equipped weapons)
                if len(player_stats["weapons"]["equipped"]) < 4:
                        player_stats["weapons"]["equipped"][w] = {"cooldown": 0}
                else:
                        player_stats["weapons"]["unequipped"].append(w)
        return player_stats, dropped_weapons

def equip_weapon(player_stats, weapon_name):
    if weapon_name in player_stats["weapons"]["unequipped"]:
        if len(player_stats["weapons"]["equipped"]) < 4:
            player_stats["weapons"]["equipped"][weapon_name] = 0  # cooldown starts at 0
            player_stats["weapons"]["unequipped"].remove(weapon_name)
            return True
        else:
            return False  # no free slot
    return False  # weapon not in unequipped

def unequip_weapon(player_stats, weapon_name):
    if weapon_name in player_stats["weapons"]["equipped"]:
        player_stats["weapons"]["unequipped"].append(weapon_name)
        del player_stats["weapons"]["equipped"][weapon_name]
        return True
    return False  # weapon not equipped

def change_weapons(player_stats, equip_name=None, unequip_name=None):
    equipped_result = None
    unequipped_result = None
    if equip_name:
        equipped_result = equip_weapon(player_stats, equip_name)
    if unequip_name:
        unequipped_result = unequip_weapon(player_stats, unequip_name)
    return equipped_result, unequipped_result

while True:
        if check != "yes":
                break
                #give the info from the beginning
        print("Welcome, lowly chicken. We are the omnnipotent, omniscient chickens. We give you a mission: You must travel to this planet and destroy it, slowly. \nYou now were hurtled into a strange room, unprepared for such an entrance. \nThere is a sword on the ground. ")
        while True:
                check = input("Do you want to pick up the sword? If so, write 'yes'. ").lower()
                if check == "yes":
                        equip_weapon(player_stats, "sword")
                        break
        while True:
                for i in enemies:
                        if i in rooms[(player_stats["location"])]:
                                enemy = i
                rooms[(player_stats["location"])][enemy] = False
                if enemy == "order_of_fights":
                        for i in range(10):
                                if rooms[(player_stats["location"])]["order_of_fights"][i][1]:
                                        enemy = rooms[(player_stats["location"])]["order_of_fights"][i][1]
                                        break
                                elif rooms[(player_stats["location"])]["order_of_fights"][i][2]:
                                        enemy = rooms[(player_stats["location"])]["order_of_fights"][i][2]
                                        break
                                elif rooms[(player_stats["location"])]["order_of_fights"][i][3]:
                                        enemy = rooms[(player_stats["location"])]["order_of_fights"][i][3]
                                        break
                else:
                        check = input("Do you want to fight one of my men? If so write '1'. ")
                        if check == "1":
                                enemy = "old"    
                if enemy == "kid":
                        enemy = {
                                "weapon": [
                                        {"name": random.choice(["sword", "axe", "spear", "club"]), "cooldown": 0}
                                ],
                                "health": 20,
                                "strength": 20
                        }
                elif enemy == "adult":
                        enemy = {
                                "weapon": [
                                        {"name": random.choice(["sword", "axe", "spear", "club"]), "cooldown": 0},
                                        {"name": random.choice(["sword", "axe", "spear", "club"]), "cooldown": 0}
                                ],
                                "health": 40,
                                "strength": 40
                        }
                elif enemy == "old":
                        enemy = {
                                "weapon": [
                                        {"name": random.choice(["sword", "axe", "spear", "club"]), "cooldown": 0},
                                        {"name": random.choice(["sword", "axe", "spear", "club"]), "cooldown": 0},
                                        {"name": random.choice(["sword", "axe", "spear", "club"]), "cooldown": 0}
                                ],
                                "health": 20,
                                "strength": 50
                        }
                elif enemy == "gatekeeper":
                        enemy = {
                                "weapon": [
                                        {"name": "axe", "cooldown": 0},
                                        {"name": "club", "cooldown": 0},
                                        {"name": "beak", "cooldown": 0}
                                ],
                                "health": 50,
                                "strength": 50
                        }
                elif enemy == "boss":
                        enemy = {
                                "weapon": [
                                        {"name": "axe", "cooldown": 0},
                                        {"name": "club", "cooldown": 0},
                                        {"name": "sword", "cooldown": 0},
                                        {"name": "spear", "cooldown": 0}
                                ],
                                "health": 60,
                                "strength": 60
                        }
                while player_stats["current_health"] > 0 and enemy["health"] > 0:
                        turn = 0
                        # Call the combat with the enemy first
                        dmg, enemy, player_stats = combat(enemy, turn, "")
                        # Display the dmg and what the enemy did
                        print(f"You took {dmg} damage. Your health is now {player_stats['current_health']}")
                        player_stats["current_health"] -= dmg
                        turn = 1
                        # Combat to give the options to the player
                        options, enemy, player_stats = combat(enemy, turn, "")
                        print("Your options are:")
                        # Infinite loop:
                        while True:
                        # Give the options to the player
                                for option in options:
                                        print(option)
                                # If the player responds with a valid response:
                                check = input("Which one do you want to choose? ")
                                if check in options:
                                        # Run combat with that new information
                                        dmg, enemy, player_stats = combat(enemy, turn, check)
                                        if dmg != "healed":
                                                print(f"The enemy took {dmg} damage. Their health is now {enemy['health']}")
                                                enemy["health"] -= dmg
                                                break
                                        else:
                                                print("You healed 10 damage")
                                                
                                                if player_stats["current_health"] + 10 < player_stats["stats"]["health"]:
                                                        player_stats["current_health"] = player_stats["stats"]["health"]
                                                else:
                                                        player_stats["current_health"] += 10
                                print("Try again. That was an invalid input. ")
                if player_stats["current_health"] <= 0:
                        check = input("You lost. Do you want to play again? If so, write 'yes'. ").lower()
                        break
                else:
                        player_stats, dropped = loot_enemy(enemy, player_stats)
                        print("You won! ")
                # Otherwise if there is a person in the room:
                if player_stats["location"] in ["bob", "mage", "bonus area 1", "bonus area 2", "shop", "gladiator ring"]:
                        # Talk with them from a dictionary with dialogue
                        for line in dialogue[player_stats["location"]]:
                                print(line)
                        # If it is the mage room and the player has not yet gotten the stat boost:
                        if player_stats["location"] == "mage" and rooms["mage"]["boost"] == "":
                                # Infinite loop:
                                while True:
                                        # Check which stat they want to boost
                                        check = input("Which stat do you want to boost? Intelligence, strength, or health").lower()
                                        # If it is a real stat:
                                        if check in ["intelligence", "strength", "health"]:
                                                # Boost that stat by 10
                                                player_stats["stats"][check] += 10
                                                # Break the loop
                                                break
                        # Otherwise if it has Bob and they have not gotten a necklace yet:
                        elif player_stats["location"] == "bob" and len(necklaces) == 3:
                                # Infinite loop:
                                while True:
                                        # Check which necklace they want
                                        print(f"Which necklace do you want? A {necklaces[0]} necklace, a {necklaces[1]} necklace, or a {necklaces[2]} necklace? ")
                                        check = input("")
                                        # If it is a real option:
                                        if check in necklaces:
                                                # Put it into the inventory
                                                player_stats["necklace"] = check
                                                player_stats["stats"][check] += 10
                                                necklaces.remove(check)
                                                # Break loop
                                                break
                        elif player_stats["location"] == "bonus area 1" and len(necklaces) == 2:
                                while True:
                                        print(f"Which necklace do you trade for? A {necklaces[0]} necklace, or a {necklaces[1]} necklace? ")
                                        check = input("")
                                        if check in necklaces:
                                                player_stats["stats"][player_stats["necklace"]] -= 10
                                                player_stats["necklace"] = check
                                                player_stats["stats"][check] += 10
                                                necklaces.remove(check)
                                                break
                        elif player_stats["location"] == "bonus area 2" and len(necklaces) == 1:
                                while True:
                                        check = input("In exchange for the supe necklace, will you trade your current necklace? If so, write 'yes'. ").lower()
                                        if check == "yes":
                                                player_stats["stats"][player_stats["necklace"]] -= 10
                                                for i in player_stats["stats"]:
                                                        player_stats["stats"][i] += 10
                                                player_stats["necklace"] = "super necklace"
                        elif player_stats["location"] == "shop":
                                while True:
                                        print("The shopkeeper squawks:")
                                        print("“I will trade 1 health potion for 1 weapon.”")
                                        # If player has no weapons
                                        if len(player_stats["weapons"]["unequipped"]) == 0:
                                                print("You have no weapons to trade.")
                                                break
                                        while True:
                                                print("\nYour unequipped weapons:")
                                                for w in player_stats["weapons"]["unequipped"]:
                                                        print("-", w)
                                                        print(f"Health potions: {player_stats['health_potions']}")
                                                        choice = input("Which weapon do you want to trade? (or type 'leave') ").lower()
                                                        if choice == "leave":
                                                                print("You leave the shop.")
                                                                break
                                                        elif choice in player_stats["weapons"]["unequipped"]:
                                                                # Remove weapon
                                                                player_stats["weapons"]["unequipped"].remove(choice)
                                                                # Give potion
                                                                player_stats["health_potions"] += 1
                                                                print(f"You traded {choice} for a health potion.")
                                                                print(f"You now have {player_stats['health_potions']} health potion(s).")
                                                        else:
                                                                print("That is not a valid weapon.")
                        elif player_stats["location"] == "resting place" and rooms["resting place"]["health potion"] == True:
                                print("You find a helath potion! ")
                                while True:
                                        check = input("Do you want to pick it up? If so, write 'yes'. ")
                                        if check == "yes":
                                                player_stats["health_potions"] += 2
                                                rooms["resting place"]["health potion"] = False
                                                break
                                        print("Try again. That input was invalid. ")
                        # Otherwise if they are in the boss room:
                        elif player_stats["location"] == "boss room":
                                # Display the information learned at the end of the game
                                print("You won the game! Good job. Welcome to the life of an omnipotent being. ")
                                # Check if the player wants to play again or leave
                                check = input("Do you want to play again? If so, write 'yes'. ")
                                break
                        check = input("Do you want to rearrange your inventory? ").lower()
                        if check == "yes":
                                while True:
                                        # Show current status
                                        print("\nEquipped weapons:", list(player_stats["weapons"]["equipped"].keys()))
                                        print("Unequipped weapons:", player_stats["weapons"]["unequipped"])
                                        print("Type 'equip <weapon>', 'unequip <weapon>', or 'done' to finish.")
                                        
                                        # Get player input
                                        choice = input("What do you want to do? ").strip().lower()
                                        
                                        if choice == "done":
                                                break
                                        
                                        if choice.startswith("equip "):
                                                weapon_name = choice.split("equip ", 1)[1]
                                                if weapon_name in player_stats["weapons"]["unequipped"]:
                                                        if len(player_stats["weapons"]["equipped"]) < 4:
                                                                player_stats["weapons"]["equipped"][weapon_name] = {"cooldown": 0}
                                                                player_stats["weapons"]["unequipped"].remove(weapon_name)
                                                                print(f"{weapon_name} equipped!")
                                                        else:
                                                                print("No free slot to equip this weapon. Unequip one first.")
                                                else:
                                                        print(f"{weapon_name} is not in your unequipped weapons.")
                                        elif choice.startswith("unequip "):
                                                weapon_name = choice.split("unequip ", 1)[1]
                                                if weapon_name in player_stats["weapons"]["equipped"]:
                                                        player_stats["weapons"]["unequipped"].append(weapon_name)
                                                        del player_stats["weapons"]["equipped"][weapon_name]
                                                        print(f"{weapon_name} unequipped!")
                                                else:
                                                        print(f"{weapon_name} is not currently equipped.")
                                        
                                        else:
                                                print("Invalid command. Use 'equip <weapon>', 'unequip <weapon>', or 'done'.")
                        # Infinite loop:
                        while True:
                                # Activate movement to get options
                                options = move("")
                                # Infinite loop:
                                while True:
                                        # Display options
                                        print("Your options are: ")
                                        for option in options:
                                                print(option)
                                        # Choose from options
                                        check = input("Which place do you want to go to? ")
                                        # Run movement
                                        if check in options:
                                                player_stats = move(check)
                                                if player_stats["location"] in ["shop", "beginning", "boss room"]:
                                                        print(rooms[player_stats["location"]])
                                                else:
                                                        if rooms[player_stats["location"]]["visited"] == False:
                                                                print(rooms[player_stats["location"]]["description 1"])
                                                        else:
                                                                print(rooms[player_stats["location"]]["description 2"])
                                                rooms[player_stats["location"]]["visited"] = True
                                                break
                                        print("Try again. Your input was invalid. ")
