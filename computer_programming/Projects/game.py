# #Final Project
# #Import the random functions
import random
necklaces = ["intelligence", "strength", "strength"]
# #Set the player stats in a definition:
player_stats = {
# 	#Stats:
"stats": {
# 		#Intelligence: 50
        "intelligence": 50,
# 		#Strength: 50
        "strength": 50,
# 		#Health: 50
        "health": 50
},
"current_health": 50,
# 	#Weapons: List of all the weapons that the player has
"weapons": {
# 	#Equipped: 
        "equipped": {
# 		#Weapon 1: cooldown
        "weapon1": 0,
# 		#Weapon 2: cooldown
        "weapon2" : 0,
# 		#Weapon 3: cooldown
        "weapon3": 0,
# 		#Weapon 4: cooldown
        "weapon4": 0
        },
        "unequipped": [],
},
# 	#Health potions: 0
"health_potions": 0,
# 	#Necklace: whichever necklace they have equipped
"necklace": "",
# 	#Location: Beginning
"location": "beginning"
}
# #Set the enemy stats in a definition:
enemies = {
# 	Kid’s stats:
"kid": {
# 		Weapon can either be sword, axe, spear, or club
        "weapon1": ["random"],
# 		Health is 20
        "health": 20,
# 		Strength is 20
        "strength": 20
        },
# 	Adult’s stats:
"adult": {
# 		Weapon can either be sword, axe, spear, or club
        "weapon1":["random", "random"],
# 		Health is 40
        "health": 40,
# 		Strength is 40
        "strength": 40
        },
# 	Old’s stats:
"old": {
# 		Weapon can either be sword, axe, spear, or club
        "weapon1": ["random", "random", "random"],
# 		Health is 20
        "health": 20,
# 		Strength is 50
        "strength": 50
        },
# 	Gatekeeper’s stats:
"gatekeeper": {
# 		Weapon is axe
        "weapon":["axe", "club", "beak"],
# 		Health is 50
        "health": 50,
# 		Strength is 50
        "strength": 50
},
# 	Boss’s stats:
        "boss":  {
# 		Weapon is axe
                "weapon": ["axe", "club", "sword", "spear"],
# 		Health is 60
                "health": 60,
# 		Strength is 60
                "strength": 60
}
}
# #Set the weapon stats in a definition(for example):
weapons = {
# 	Beak
        "beak": {
# 		Damage is 1
                "dmg": 1,
# 		Cooldown is 0
                "cooldown": 0
        },
# 	Sword:
        "sword": {
# 		Damage is 5
                "dmg": 5,
# 		Cooldown is 2
                "cooldown": 2
        },
# 	Axe:
        "axe": {
# 		Damage is 6
                "dmg": 6,
# 		Cooldown is 4
                "cooldown": 4
        },
# 	Spear:
        "spear": {
# 		Damage is 3
                "dmg": 3,
# 		Cooldown is 1
                "cooldown": 1
        },
# 	Club:
        "club": {
# 		Damage is 4
                "dmg": 4,
# 		Cooldown is 3
                "cooldown": 3
        },
# 	Health potion:
        "hp potion": {
# 		Heals 10 health
                "heal": 10,
# 		Cooldown is 0
                "cooldown": 0
        },
# 	Health necklace:
        "health necklace": {
# 		Adds 20 health
                "health": 20
        },
# 	Strength necklace:
        "strength necklace": {
# 		Adds 20 strength
                "strength": 20
        },
# 	Intelligence necklace:
        "intelligence necklace": {
# 		Adds 20 intelligence
                "intelligence": 20
        },
# 	Super necklace:
        "super necklace": {
# 		Adds 20 health
                "health": 20,
# 		Adds 20 strength
                "strength": 20,
# 		Adds 20 intelligence
                "intelligence": 20
        }
}

# Set the rooms in a definition:
rooms = {
# 	Beginning:
        "beginning": {
# 		Possible places to move to: bob, bonus area 1, tutorial
                "possibilities": ["bob", "bonus area 1", "tutorial"],
# 		Sword has been taken
                "sword": "",
# 		Description: You return to the place where you woke up. You look around, remembering that the omnipotent and omniscient chickens have sent you down with a purpose, to destroy Earth. 
                "description 1": "You return to the place where you woke up. You look around, remembering that the omnipotent and omniscient chickens have sent you down with a purpose, to destroy Earth. ",
                "visited": ""
        },
# 	Tutorial:
        "tutorial": {
# 		Possible places to move to: beginning, bob, gladiator ring, shop
                "possibilities": ["beginning", "bob", "gladiator ring", "shop"],
# 		Kid has not been killed
                "kid": "",
# 		Description 1: You enter a room with a kid in the center. The kid runs up at you and starts attacking you. Prepare for combat. 
                "description 1": "You enter a room with a kid in the center. The kid runs up at you and starts attacking you. Prepare for combat. ",
# 		Description 2: You enter a room with a dead kid in the center. You see the spilled blood on the floor. The walls are covered in a beautiful mosaic of Bob. 
                "description 2": "You enter a room with a dead kid in the center. You see the spilled blood on the floor. The walls are covered in a beautiful mosaic of Bob. ",
                "visited": ""
        },
# 	Bob:
        "bob": {
# 		Possible places to move to: beginning, tutorial, boss room
                "possibilities": ["beginning", "tutorial", "boss room"],
# 		Description 1: A chicken sits there, fingering his sword. He waits for you to approach him, holding some necklaces. 
                "description 1": "A chicken sits there, fingering his sword. He waits for you to approach him, holding some necklaces. ",
# 		Description 2: Bob sits there, waiting for you to approach him. It seems he wishes for you to stay away from that room with arcane energy pulsing through. 
                "description 2": "Bob sits there, waiting for you to approach him. It seems he wishes for you to stay away from that room with arcane energy pulsing through. ",
                "visited": ""
        },
# 	Gladiator Ring:
        "gladiator ring": {
# 		Possible places to move to: tutorial, shop, mage, bonus area 1, bonus area 2
                "possibilities": ["tutorial", "shop", "mage", "bonus area 1", "bonus area 2"],
# 		Order of fights
                "order of fights": {
# 		Kid has been fought
                        1: ["kid"],
# Kid, kid has not been fought
                        2: ["kid", "kid"],
# Adult has not been fought
                        3: ["adult"],
# Kid, adult has not been fought
                        4: ["kid", "adult"],
# Adult, adult has not been fought
                        5: ["adult", "adult"],
# Opens bonus area 1 has not been unlocked
                        "bonus area 1": "",
# Kid, old has not been fought
                        6: ["kid", "old"],
# Adult, old has not been fought
                        7: ["adult", "old"],
# Old, old has not been fought
                        8: ["old", "old"],
# Adult, adult, adult has not been fought
                        9: ["adult", "adult", "adult"],
                        10: ["old", "old", "old"],
# 	Opens bonus area 2 has not been unlocked
                        "bonus area 2": ""
                },
# 		Description 1: A chicken with a boisterous voice welcomes you to his arena, seeking entertainment. He decides to have you battle some of his slaves to give him entertainment. 
                "description 1": "A chicken with a boisterous voice welcomes you to his arena, seeking entertainment. He decides to have you battle some of his slaves to give him entertainment. ",
# 		Description 2: The man asks you whether you want to fight another family member or leave. 
                "description 2": "The man asks you whether you want to fight another family member or leave. ",
                "visited": ""
        },
# 	Shop:
        "shop": {
# 		Possible places to move to: bob, tutorial, gladiator ring, mage
                "possibilities": ["bob", "tutorial", "gladiator ring", "mage"],
# 		Description: You find a strange chicken with a bunch of weapons. The chicken seems to wish for something. She awaits your approach. 
                "description 1": "You find a strange chicken with a bunch of weapons. The chicken seems to wish for something. She awaits your approach. ",
                "visited": ""
        },
# 	Mage:
        "mage": {
# 		Possible places to move to: gladiator ring, shop, gatekeeper
                "possibilities": ["gladiator ring", "shop", "gatekeeper"],
# 		Boost is not given
                "boost": "",
# 		Description 1: A floating chicken stands in the center of the room, walking around. They turn to face you while they stay still, watching you. 
                "description 1": "A floating chicken stands in the center of the room, walking around. They turn to face you while they stay still, watching you. ",
# 		Description 2: The mage waits while floating at the top of the room, running along the ground, at the center of the edge of the center of the room. 
                "description 2": "The mage waits while floating at the top of the room, running along the ground, at the center of the edge of the center of the room. "
        },
# 	Gatekeeper:
        "gatekeeper": {
# 		Possible places to move to: shop, mage, resting place:
                "possibilities": ["shop", "mage", "resting place"],
                "gatekeeper": "",
# 		Description 1: A chicken, seeming to be using arcane energy from the room ahead, floats up and flies towards you. 
                "description 1": "A chicken, seeming to be using arcane energy from the room ahead, floats up and flies towards you. ",
# 		Description 2: The gatekeeper lies on the ground, dead. 
                "description 2": "The gatekeeper lies on the ground, dead. ",
                "visited": ""
        },
# Resting place:
        "resting place": {
# 		Possible places to move to: gatekeeper, boss room
                "possibilities": ["gatekeeper", "boss room"],
# 		Health potion has not been picked up
                "health potion": "",
# Description 1: You see a health potion on the ground, and only one way to go; forward. 
                "description 1": "You see a health potion on the ground, and only one way to go; forward. ",
# 		Description 2: You see the way that you should go: forward. 
                "description 2": "You see the way that you should go: forward. ",
                "visited": ""
        },
# Boss room:
        "boss room": {
# 		Possible places to move to: bob, gatekeeper
                "possibilities": ["bob", "gatekeeper"],
# 		Description 1: A door slams behind you, locking you into the room. The Chickens look at you, seeming prepared. One speaks, saying, “We may not be omniscient, but we are omnipotent. If you survive the final trial, Us, while we don’t really try, you may ascend up and join us in our pursuit of omniscience.”
                "description 1": "A door slams behind you, locking you into the room. The Chickens look at you, seeming prepared. One speaks, saying, \“We may not be omniscient, but we are omnipotent. If you survive the final trial, Us, while we don’t really try, you may ascend up and join us in our pursuit of omniscience.\”",
                "visited": ""
        },
# Bonus area 1:
        "bonus area 1": {
# 		Possible places to move to: gladiator ring
                "possibilities": ["gladiator ring"],
# 		Intelligence necklace has been taken
                "intelligence necklace": "",
# 		Health necklace has been taken
                "health necklace": "",
# 		Strength necklace has not been taken
                "strength necklace": "",
# Description 1: You see the great and glorious Bob again, waiting with his necklaces. 
                "description 1": "You see the great and glorious Bob again, waiting with his necklaces. ",
# 		Description 2: Bob, bored, asks why you are here and to shut the nonexistent door on the way out. 
                "description 2": "Bob, bored, asks why you are here and to shut the nonexistent door on the way out. ",
                "visited": ""
        },
# Bonus area 2:
        "bonus area 2": {
# 		Possible places to move to: gladiator ring, beginning
                "possibilities": ["gladiator ring", "beginning"],
# 		Description 1: Bob welcomes you, and gives you a weird necklace after taking yours. He then says “Out! My life’s goal is complete: To eat a necklace worn by a chicken! Now I have two to eat! ”
                "description 1": "Bob welcomes you, and gives you a weird necklace after taking yours. He then says \“Out! My life’s goal is complete: To eat a necklace worn by a chicken! Now I have two to eat! \”",
# 		Description 2: Bob greets you with a cheerful “SHUT THE (nonexistent) DOOR ON YOUR WAY OUT!”
                "description 2": "Bob greets you with a cheerful \“SHUT THE (nonexistent) DOOR ON YOUR WAY OUT!\”",
                "visited": ""
        },
}

dialouge = {
        "bob": {
                1: "Hello. Welcome. ",
                2: "Would you like a necklace? ",
                3: "I have a neat selection of them. ",
                4: "I have this one that boosts you intelligence, one that boosts your strength, and one that boosts your health. ",
                5: "So, which one do you want? ",
        },
        "shop": {
                1: "Welcome, welcome. ",
                2: "I exchange weapons for some potions I make. ",
                3: "Do you want some? "
        },
        "gladiator ring": {
                1: "Welcome, pitiful being. ",
                2: "I have some humans for you to fight, if you wish to fight them. "
        },
        "mage": {
                1: "Welcome good sir. ",
                2: "I like you. Do you want a boost of your strength, intelligence, or health? ",
        },
        "bonus area 1": {
                1: "Welcome, let me take this necklace of your shoulders. ",
                2: "Just kidding, I have another necklace. ",
                3: "Which one do you want now? "
        },
        "bonus area 2": {
                1: "Hello. ",
                2: "I will take these necklaces off your shoulders now. ",
                3: "Here is the super necklace, it combines intelligence, health, and strength boost in one. "
        }
}

# Set the combat as a function and the parameters as: enemy, info about all enemies, player health, player strength, the list of equipped items, the weapon(s) the enemy has, the enemy’s health, whose turn it is, which weapon the player wants to attack with:
def combat(enemy, player_stats, turn, weapon, weapons):
        possibilities = []
# If the enemy is attacking:
        if turn == 0:
# See how many available weapons the enemy has and store that in a variable
                weapons = len(enemy["weapon"])
# If they have some:
                for i in range(weapons):
                        if enemy["weapon"][i] == 0:
                                possibilities.append(enemy["weapon"][i])
                        else:
                                enemy["weapon"][i] - 1
# 	Infinite loop:
                        while True:
# 	Pick a random weapon option
                                weapon_choice = random.choice(possibilities)
# 			Calculate the damage as ((strength / 100) + 1) * dmg_of_weapon
                                dmg = ((enemy["strength"] / 100) + 1) * weapons[weapon_choice]["dmg"]
# 			Set the weapon that you just used to their respective 	cooldown
                                enemy["weapon"][weapon_choice] = weapons[weapon_choice]["cooldown"]
                                player_stats["current_health"] -= dmg
# 			Return the damage
                                return(dmg, enemy, player_stats)
# 	Otherwise if the player is attacking:
        else:
                for i in player_stats["weapons"]:
                        if player_stats["weapons"][i] == 0:
                                possibilities.append(player_stats["weapons"][i])
# 		If the player didn’t input a weapon yet
                if weapon == "":
# 		If the player has no possible weapons
# 				Return by give them one option; to attack with the beak
                        if  possibilities == []:
                                return(["beak"])
# Otherwise:
                        else:
# 		If the player has health potions:
                                if player_stats["health_potions"] > 0:
# 			Add it to the list
                                        possibilities.append()
# 		Return the list
                        return(possibilities)
# Otherwise if they inputted a weapon:
                elif weapon in ["sword", "axe", "club", "spear", "beak"]:
# 	Calculate the damage as ((strength / 100) + 1) * dmg_of_weapon
                        dmg = ((player_stats["strength"] / 100) + 1) * weapons[weapon]["dmg"]
# 	If any cooldowns are bigger than 0:
                        for i in range(4):
                                if player_stats["weapons"][i] > 0:
# 		Subtract 1 from each of those
                                        player_stats["weapons"][i] - 1
# 	Set the cooldown to its respective time
                        player_stats["weapons"][weapon] = weapons[weapon]["cooldown"]
                        enemy["health"] -= dmg
# 	Return the damage
                        return(dmg)
# Otherwise if they inputted a health potion:
                else:
# 	Add 10 health to the player’s health
                        if (player_stats["current_health"] + 10) > player_stats["stats"]["health"]:
                                
# 	If any cooldowns are bigger than 0:
# 		Subtract 1 from each of those
# 	Return that

# Set the movement as a function and the parameters as: current room, definition of the rooms, where they want to go:
# 	Check to see all the different possible rooms. 
# 	If they have not inputted a room that they want to go to:
# 		Return the possible rooms
# If they give a feasible location to go:
# 	Set the player’s location to there
# 	If there is a first description:
# Do the first description
# Erase the first description
# 	Otherwise:
# 		Send the second description
# 	Change the location to visited
# 	Check if there is an item on the ground
# 	Return the information to the normal game
# Otherwise:
# 	Return the information to the game that they failed in choosing the next area and the possible rooms
# Set the conversation with the mage as a function and the parameters as: player stats
# 	Check if the player has inputted a feasible choice:
# 		Return that stat as boosted
# 	Return the options

# Infinite loop:
# 	Give the whole background information
# 	Infinite loop
# 	Ask if the player wants to take the sword of the ground
# 	If so:
# 		Change its thing to taken
# 		Break the loop
# 	Otherwise:
# 		Say try again
# 	If there is an enemy in the room:
# 		Infinite loop:
#asign the weapon and stuff to the enemy
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
                "weapon": {
                        random.choice["sword", "spear", "axe", "club"]: 0
                },
# 		Health is 20
                "health": 20,
# 		Strength is 20
                "strength": 20
        }
elif enemy == "adult":
        enemy = {
                "weapon": {
                        random.choice["sword", "spear", "axe", "club"]: 0,
                        random.choice["sword", "spear", "axe", "club"]: 0
                },
                "health": 40,
                "strength": 40
        }
elif enemy == "old":
        enemy = {"weapon": {
                        random.choice["sword", "spear", "axe", "club"]: 0,
                        random.choice["sword", "spear", "axe", "club"]: 0,
                        random.choice["sword", "spear", "axe", "club"]: 0
                },
                "health": 20,
                "srength": 50
        }
elif enemy == "gatekeeper":
        enemy = {
                "weapon": {
                        "axe": 0,
                        "club": 0,
                        "beak": 0
                },
                "health": 50,
                "strength": 50
        }
while True:
        if 
                while True:
                        # Call the combat with the enemy first
                        turn = 0
                        dmg, enemy, player_stats = combat(enemy, enemies, player_stats, turn, "", weapons)
                        # Display the dmg and what the enemy did
                        print(f"You took {dmg} damage. Your health is now {player_stats["health"]}. ")
                        if player_stats["current_health"] <= 0:
                                print("You lost!!! ")
                                lose = True
                                break
                        # Combat to give the options to the player
                        turn = 1
                        options = combat()
                        # Infinite loop:
                        while True:
                        # 	Give the options to the player
                                print(f"Your options are {options}. ")
                                check = input("Which one do you want? write the corresponding location. ")
                        # 	If the player responds with a valid response:
                                if check in options:
                        # 		Run combat with that new information
                                        dmg, player_stats, enemy = combat(enemy, player_stats, turn, check, weapons)
                        # 		Break the loop
                                        break
                                print("Try again. You inputted a wrong input. ")
                        if enemy["health"] <= 0:
                                print("You won!!! ")
                                break
                if lose == True:
                        print("You lost. \nDo you want to play again? ")
                        check = input("If so, write 1. ")
                        if check == "1":
                                break
                        
# 	Otherwise if there is a person in the room:
        elif player_stats["location"] in ["mage", "bob", "gladiator ring", "shop", "bonus area 1", "bonus area 2"]:
# 		Talk with them from a dictionary with dialogue
                for i in len(dialouge[player_stats["location"]]):
                        print(dialouge[player_stats["location"]][i])
# 		If it is the mage room and the player has not yet gotten the stat boost:
                if player_stats["location"] == "mage" and rooms["mage"]["boost"] == "":
# 			Infinite loop:
                        while True:
# 				Check if the player wants to get a stat boost
                                check = input("So, which do you want? intelligence, strength, or health. ")
# 				If so:
                                if check in ["intelligence", "strength", "health"]:
# 				        Boost that stat by 10
                                        player_stats["stats"][check] += 10
# 							Break the loop
                                        break
                                print("Try again. That was an invalid input. ")
# 		Otherwise if it has Bob and they have not gotten a necklace from that room yet:
                elif player_stats["location"] == "bob" and len(necklaces) == 3:
# 			Infinite loop:
                        while True:
# 				Check which necklace they want
                                check = input(f"So, which do you want? A {necklaces[0]} necklace, a {necklaces[1]} necklace, or a {necklaces[2]} necklace. ")
# 				If it is a real option:
                                if check in necklaces:
# 					Put it into the player’s inventory
                                        player_stats["neacklace"] = check
# 					Break the infinite loop
                                        break
                                print("Try again. That was an invalid input. ")
                elif player_stats["location"] == "bonus area 1" and len(necklaces) == 2:
# 			Infinite loop:
                        while True:
# 				Check which necklace they want
                                check = input(f"So, which do you want? A {necklaces[0]} necklace or a {necklaces[1]} necklace. ")
# 				If it is a real option:
                                if check in necklaces:
# 					Put it into the player’s inventory
                                        player_stats["neacklace"] = check
# 					Break the infinite loop
                                        break
                                print("Try again. That was an invalid input. ")
                elif player_stats["location"] == "bonus area 2" and len(necklaces) == 2:
# 			Infinite loop:
                        while True:
# 				Check which necklace they want
                                check = input(f"So, which do you want? A {necklaces[0]} necklace or a {necklaces[1]} necklace. ")
# 				If it is a real option:
                                if check in necklaces:
# 					Put it into the player’s inventory
                                        player_stats["neacklace"] = check
# 					Break the infinite loop
                                        break
                                print("Try again. That was an invalid input. ")
# 	Otherwise if they are in the boss room:
                elif player_stats["location"] == "boss room":
# 		(The combat will run because the Chickens are an enemy)
# 		Display the information that they learn at the end of the game(This part comes after combat)
# 	Check if the player wants to play again or leave the game
# 		If they want to leave the game:
# 			Break the loop
# 		Otherwise:
# 			Restart the game
# 	Infinite loop:
# 		Activate the movement function to get the options
# 		Infinite loop:
# 			Display the options
# 			Have the player choose from the options
# 			Run the movement function
# 			If the input was valid:
# 				Break the loop
# 		If the player moved:
# 			Break the loop
# 		Show the options
# 		Check which one the player want to use



