# Final Project

# Import the random functions
import random

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
                "health": 50
        },
        "current_health": 50,
        # Weapons: List of all the weapons that the player has
        "weapons": {
                # Equipped:
                "equipped": {
                        # Weapon 1: cooldown
                        "weapon1": 0,
                        # Weapon 2: cooldown
                        "weapon2": 0,
                        # Weapon 3: cooldown
                        "weapon3": 0,
                        # Weapon 4: cooldown
                        "weapon4": 0
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
                # Weapon can either be sword, axe, spear, or club
                "weapon1": ["random"],
                # Health is 20
                "health": 20,
                # Strength is 20
                "strength": 20
        },

        # Adult’s stats:
        "adult": {
                # Weapon can either be sword, axe, spear, or club
                "weapon1": ["random", "random"],
                # Health is 40
                "health": 40,
                # Strength is 40
                "strength": 40
        },

        # Old’s stats:
        "old": {
                # Weapon can either be sword, axe, spear, or club
                "weapon1": ["random", "random", "random"],
                # Health is 20
                "health": 20,
                # Strength is 50
                "strength": 50
        },

        # Gatekeeper’s stats:
        "gatekeeper": {
                # Weapon is axe
                "weapon": ["axe", "club", "beak"],
                # Health is 50
                "health": 50,
                # Strength is 50
                "strength": 50
        },

        # Boss’s stats:
        "boss": {
                # Weapon is axe
                "weapon": ["axe", "club", "sword", "spear"],
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
        "hp potion": {
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
                "visited": ""
        },

        # Tutorial:
        "tutorial": {
                # Possible places to move to: beginning, bob, gladiator ring, shop
                "possibilities": ["beginning", "bob", "gladiator ring", "shop"],
                # Kid has not been killed
                "kid": "",
                # Description 1:
                "description 1": "You enter a room with a kid in the center. The kid runs up at you and starts attacking you. Prepare for combat. ",
                # Description 2:
                "description 2": "You enter a room with a dead kid in the center. You see the spilled blood on the floor. The walls are covered in a beautiful mosaic of Bob. ",
                "visited": ""
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
                "visited": ""
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
                "visited": ""
        },

        # Shop:
        "shop": {
                "possibilities": ["bob", "tutorial", "gladiator ring", "mage"],
                "description 1": "You find a strange chicken with a bunch of weapons. The chicken seems to wish for something. She awaits your approach. ",
                "visited": ""
        },

        # Mage:
        "mage": {
                "possibilities": ["gladiator ring", "shop", "gatekeeper"],
                "boost": "",
                "description 1": "A floating chicken stands in the center of the room, walking around. They turn to face you while they stay still, watching you. ",
                "description 2": "The mage waits while floating at the top of the room, running along the ground, at the center of the edge of the center of the room. "
        },

        # Gatekeeper:
        "gatekeeper": {
                "possibilities": ["shop", "mage", "resting place"],
                "gatekeeper": "",
                "description 1": "A chicken, seeming to be using arcane energy from the room ahead, floats up and flies towards you. ",
                "description 2": "The gatekeeper lies on the ground, dead. ",
                "visited": ""
        },

        # Resting place:
        "resting place": {
                "possibilities": ["gatekeeper", "boss room"],
                "health potion": "",
                "description 1": "You see a health potion on the ground, and only one way to go; forward. ",
                "description 2": "You see the way that you should go: forward. ",
                "visited": ""
        },

        # Boss room:
        "boss room": {
                "possibilities": ["bob", "gatekeeper"],
                "description 1": "A door slams behind you, locking you into the room. The Chickens look at you, seeming prepared. One speaks, saying, “We may not be omniscient, but we are omnipotent. If you survive the final trial, Us, while we don’t really try, you may ascend up and join us in our pursuit of omniscience.”",
                "visited": ""
        },

        # Bonus area 1:
        "bonus area 1": {
                "possibilities": ["gladiator ring"],
                "intelligence necklace": "",
                "health necklace": "",
                "strength necklace": "",
                "description 1": "You see the great and glorious Bob again, waiting with his necklaces. ",
                "description 2": "Bob, bored, asks why you are here and to shut the nonexistent door on the way out. ",
                "visited": ""
        },

        # Bonus area 2:
        "bonus area 2": {
                "possibilities": ["gladiator ring", "beginning"],
                "description 1": "Bob welcomes you, and gives you a weird necklace after taking yours. He then says “Out! My life’s goal is complete: To eat a necklace worn by a chicken! Now I have two to eat! ”",
                "description 2": "Bob greets you with a cheerful “SHUT THE (nonexistent) DOOR ON YOUR WAY OUT!”",
                "visited": ""
        },
}

dialogue = {
        "bob": [],
        "mage": [],
        "shop": [],
        "gladiator ring": [],
        "bonus area 1": [],
        "bonus area 2": []
        
}

# Set the combat as a function and the parameters as: enemy, info about all enemies, player health, player strength, the list of equipped items, the weapon(s) the enemy has, the enemy’s health, whose turn it is, which weapon the player wants to attack with:
def combat(enemy, enemies, player_stats, turn, weapon):
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
            # If that corresponds with an available weapon:
            # Calculate the damage as ((strength / 100) + 1) * dmg_of_weapon
            damage = ((enemy["strength"] / 100) + 1) * enemy["weapon"][weapon_choice]["damage"]
            # Drop each cooldown drop by one
            for w in enemy["weapon"]:
                if w["cooldown"] > 0:
                    w["cooldown"] -= 1
            # Set the weapon that you just used to their respective cooldown
            enemy["weapon"][weapon_choice]["cooldown"] = enemy["weapon"][weapon_choice]["max_cooldown"]
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
            damage = ((player_stats["stats"]["strength"] / 100) + 1) * player_stats["weapons"]["equipped"][weapon]["damage"]
            # If any cooldowns are bigger than 0:
            for w in player_stats["weapons"]["equipped"]:
                if player_stats["weapons"]["equipped"][w]["cooldown"] > 0:
                    player_stats["weapons"]["equipped"][w]["cooldown"] -= 1
            # Set the cooldown to its respective time
            player_stats["weapons"]["equipped"][weapon]["cooldown"] = player_stats["weapons"]["equipped"][weapon]["max_cooldown"]
            # Return the damage
            return damage, enemy, player_stats
        # Otherwise if they inputted a health potion:
        elif weapon == "health potion" and player_stats["items"].get("health potion", 0) > 0:
            # Add 10 health to the player’s health
            player_stats["current_health"] += 10
            player_stats["items"]["health potion"] -= 1
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
        if player_stats["items"].get("health potion", 0) > 0:
            # Add it to the list
            usable_options.append("health potion")
        # Return the list
        return usable_options, enemy, player_stats

while True:
    for i in ["kid", "adult", "old", "order_of_fights", "gatekeeper"]:
            if i in rooms[(player_stats["location"])]:
                    enemy = i
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
                    random.choice["sword", "spear", "axe", "club"]: 0,
                    "health": 20,
                    "strength": 20
            }
    elif enemy == "adult":
            enemy = {
                    random.choice["sword", "spear", "axe", "club"]: 0,
                    random.choice["sword", "spear", "axe", "club"]: 0,
                    "health": 40,
                    "strength": 40
            }
    elif enemy == "old":
            enemy = {
                    random.choice["sword", "spear", "axe", "club"]: 0,
                    random.choice["sword", "spear", "axe", "club"]: 0,
                    random.choice["sword", "spear", "axe", "club"]: 0,
                    "health": 20,
                    "srength": 50
            }
    elif enemy == "gatekeeper":
            enemy = {
                    "axe": 0,
                    "club": 0,
                    "beak": 0,
                    "health": 50,
                    "strength": 50
            }
    while True:
            # Call the combat with the enemy first
            dmg, enemy, player_stats = combat(enemy, enemies, player_stats, turn, "")
            # Display the dmg and what the enemy did
            print(f"You took {dmg} damage. Your health is now {player_stats}")
            # Combat to give the options to the player
            # Infinite loop:
            # Give the options to the player
            # If the player responds with a valid response:
            # Run combat with that new information
            # Break the loop
    
            break
    
        # Otherwise if there is a person in the room:
        elif player_stats["location"] in ["bob", "mage", "bonus area 1", "bonus area 2", "shop", "gladiator ring"]
                # Talk with them from a dictionary with dialogue
                for i in dialogue[player_stats["location"]]:
                        print(dialogue[player_stats["location"][i-1]])
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
                                print(f"Which necklace do you want? A {necklaces[0]} necklace, a {necklaces[1]} necklace, or a {necklaces{2} necklace? ")
                                check = input("")
                                # If it is a real option:
                                if check in necklaces:
                                        # Put it into the inventory
                                        player_stats["necklace"] = check
                                        necklace.pop(check)
                                        # Break loop
                                        break
                # Otherwise if they are in the boss room:
                elif player_stats["location"] == "boss room":
                # The combat will run
                        
                # Display the information learned at the end of the game
                # Check if the player wants to play again or leave
                # If leave: break
                # Otherwise restart
                # Infinite loop:
        # Activate movement to get options
        # Infinite loop:
        # Display options
        # Choose from options
        # Run movement
        # If valid: break
        # If moved: break
        # Show options
        # Check which one the player wants to use
