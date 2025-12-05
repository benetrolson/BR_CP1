# #Final Project
# #Import the random functions
import random
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
    "location": "Beginning"
    }
# #Set the enemy stats in a definition:
enemies = {
# 	Kid’s stats:
    "kid": {
# 		Weapon can either be sword, axe, spear, or club
        "weapon1": random.choice["sword", "spear", "axe", "club"],
# 		Health is 20
        "health": 20,
# 		Strength is 20
        "strength": 20
        },
# 	Adult’s stats:
    "adult": {
# 		Weapon can either be sword, axe, spear, or club
        "weapon1": random.choice["sword", "spear", "axe", "club"],
#       Weapon can either be sword, axe, spear, or club
        "weapon2": random.choice["sword", "spear", "axe", "club"],
# 		Health is 40
        "health": 40,
# 		Strength is 40
        "strength": 40
        },
# 	Old’s stats:
    "old": {
# 		Weapon can either be sword, axe, spear, or club
        "weapon1": random.choice["sword", "spear", "axe", "club"],
#       Weapon can either be sword, axe, spear, or club
        "weapon2": random.choice["sword", "spear", "axe", "club"],
# 		Weapon can either be sword, axe, spear, or club
        "weapon3": random.choice["sword", "spear", "axe", "club"],
# 		Health is 20
        "health": 20,
# 		Strength is 50
        "strength": 50
        },
# 	Gatekeeper’s stats:
# 		Weapon is axe
# #Weapon is club
# #Weapon is beak
# 		Health is 50
# 		Strength is 50
# 	Boss’s stats:
# 		Weapon is axe
# #Weapon is club
# #Weapon is sword
# #Weapon is spear
# #Weapon is beak
# 		Health is 60
# 		Strength is 60
    }
# #Set the weapon stats in a definition(for example):
# 	Beak
# 		Damage is 1
# 		Cooldown is 0
# 	Sword:
# 		Damage is 5
# 		Cooldown is 2
# 	Axe:
# 		Damage is 6
# 		Cooldown is 4
# 	Spear:
# 		Damage is 3
# 		Cooldown is 1
# 	Club:
# 		Damage is 4
# 		Cooldown is 3
# 	Health potion:
# 		Heals 10 health
# 		Cooldown is 0
# 	Health necklace:
# 		Adds 20 health
# 		Cooldown is 0
# 	Strength necklace:
# 		Adds 20 strength
# 		Cooldown is 0
# 	Intelligence necklace:
# 		Adds 20 intelligence
# 		Cooldown is 0
# 	Super necklace:
# 		Adds 20 health
# 		Adds 20 strength
# 		Adds 20 intelligence

# Set the rooms in a definition:
# 	Beginning:
# 		Possible places to move to:
# 		Bob’s room has not been visited
# 			Bonus area is locked
# 			Tutorial room has not been visited
# 		Sword has been taken
# 		Description: You return to the place where you woke up. You look around, remembering that the omnipotent and omniscient chickens have sent you down with a purpose, to destroy Earth. 
# 	Tutorial:
# 		Possible places to move to:
# 			Beginning has been visited
# 			Bob has not been visited
# 			Gladiator ring has not been visited
# 			Shop has not been visited
# 		Kid has not been killed
# 		Description 1: You enter a room with a kid in the center. The kid runs up at you and starts attacking you. Prepare for combat. 
# 		Description 2: You enter a room with a dead kid in the center. You see the spilled blood on the floor. The walls are covered in a beautiful mosaic of Bob. 
# 	Bob:
# 		Possible places to move to:
# 			Beginning room has been visited
# 			Tutorial room has been visited
# 			Boss room has not been visited
# 		Intelligence necklace has been taken
# 		Health necklace has not been taken
# 		Strength necklace has not been taken
# 		Description 1: A chicken sits there, fingering his sword. He waits for you to approach him, holding some necklaces. 
# 		Description 2: Bob sits there, waiting for you to approach him. It seems he wishes for you to stay away from that room with arcane energy pulsing through. 
# 	Gladiator Ring:
# 		Possible places to move to:
# 		Tutorial room has been visited
# 		Shop has been visited
# 			Mage has not been visited
# 			Bonus area is locked
# 			Bonus area is locked
# 		Order of fights
# 		Kid has been fought
# Kid, kid has not been fought
# Adult has not been fought
# Kid, adult has not been fought
# Adult, adult has not been fought
# Opens bonus area 1 has not been unlocked
# Kid, old has not been fought
# Adult, old has not been fought
# Old, old has not been fought
# Adult, adult, adult has not been fought
# 	Opens bonus area 2 has not been unlocked
# 		Description 1: A chicken with a boisterous voice welcomes you to his arena, seeking entertainment. He decides to have you battle some of his slaves to give him entertainment. 
# 		Description 2: The man asks you whether you want to fight another family member or leave. 
# 	Shop:
# 		Possible places to move to:
# 		Bob’s room has been visited
# 		Tutorial room has been visited
# 		Gladiator ring has been visited
# 			Mage has not been visited
# 		Description: You find a strange chicken with a bunch of weapons. The chicken seems to wish for something. She awaits your approach. 
# 	Mage:
# 		Possible places to move to:
# 			Gladiator ring has been visited
# 			Shop has been visited
# 			Gatekeeper has not been visited
# 		Boost is not given
# 		Description 1: A floating chicken stands in the center of the room, walking around. They turn to face you while they stay still, watching you. 
# 		Description 2: The mage waits while floating at the top of the room, running along the ground, at the center of the edge of the center of the room. 
# 	Gatekeeper:
# 		Possible places to move to:
# 			Shop has been visited
# 			Mage has been visited
# 			Resting place has not been visited
# 		Gatekeeper has not been killed
# 		Description 1: A chicken, seeming to be using arcane energy from the room ahead, floats up and flies towards you. 
# 		Description 2: The gatekeeper lies on the ground, dead. 
# Resting place:
# 		Possible places to move to:
# 			Gatekeeper has been visited
# 			Boss room has not been visited
# 		Health potion has not been picked up
# Description 1: You see a health potion on the ground, and only one way to go; forward. 
# 		Description 2: You see the way that you should go; forward 
# Boss room:
# 		Possible places to move to:
# 			Bob has been visited
# 			Gatekeeper has been visited
# 		Description 1: A door slams behind you, locking you into the room. The Chickens look at you, seeming prepared. One speaks, saying, “We may not be omniscient, but we are omnipotent. If you survive the final trial, Us, while we don’t really try, you may ascend up and join us in our pursuit of omniscience.”
# Bonus area 1:
# 		Possible places to move to:
# 			Gladiator ring has been visited
# 		Intelligence necklace has been taken
# 		Health necklace has been taken
# 		Strength necklace has not been taken
# Description 1: You see the great and glorious Bob again, waiting with his necklaces. 
# 		Description 2: Bob, bored, asks why you are here and to shut the nonexistent door on the way out.  
# Bonus area 2:
# 		Possible places to move to:
# 			Gladiator ring has been visited
# 			Beginning has been visited
# 		Description 1: Bob welcomes you, and gives you a weird necklace after taking yours. He then says “Out! My life’s goal is complete: To eat a necklace worn by a chicken! Now I have two! ”
# 		Description 2: Bob greets you with a cheerful “SHUT THE (nonexistent) DOOR ON YOUR WAY OUT!”
	
# Set the combat as a function and the parameters as: enemy, info about all enemies, player health, player strength, the list of equipped items, the weapon(s) the enemy has, the enemy’s health, whose turn it is, which weapon the player wants to attack with:
# If the enemy is attacking:
# The attacker is the enemy
# See how many available weapons the enemy has and store that in a variable
# If they have none:
# 	They do nothing
# Otherwise:
# 	Infinite loop:
# 	Pick a random number between 1 and 4
# 		If that corresponds with an available weapon:
# 			Calculate the damage as ((strength / 100) + 1) * dmg_of_weapon
			
# 			Drop each cooldown drop by one
# 			Set the weapon that you just used to their respective 	cooldown
# 			Return the damage
# 	Otherwise if the player is attacking:
# 		If the player didn’t input a weapon yet
# 		If the player has no possible weapons
# 				Return by give them one option; to attack with the beak
# Otherwise:
# 		Loop 4 times:
# 			If the weapon is usable:
# 				Add it to a list
# 		If the player has health potions:
# 			Add it to the list
# 		Return the list
# Otherwise if they inputted a weapon:
# 	Calculate the damage as ((strength / 100) + 1) * dmg_of_weapon
# 	If any cooldowns are bigger than 0:
# 		Subtract 1 from each of those
# 	Set the cooldown to its respective time
# 	Return the damage
# Otherwise if they inputted a health potion:
# 	Add 10 health to the player’s health
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
# Call the combat with the enemy first
# Display the dmg and what the enemy did
# Combat to give the options to the player
# Infinite loop:
# 	Give the options to the player
# 	If the player responds with a valid response:
# 		Run combat with that new information
# 		Break the loop
# 	Otherwise if there is a person in the room:
# 		Talk with them from a dictionary with dialogue
# 		If it is the mage room and the player has not yet gotten the stat boost:
# 			Infinite loop:
# 				Check if the player wants to get a stat boost
# 				If so:
# 					Infinite loop:
# 						Check which stat they want to boost
# 						If it is a real stat:
# 							Boost that stat by 10
# 							Break the loop
# 		Otherwise if it has Bob and they have not gotten a necklace from that room yet:
# 			Check if the player wants a necklace:
# 			If so:
# 				Infinite loop:
# 					Check which necklace they want
# 					If it is a real option:
# 						Put it into the player’s inventory
# 						Break the infinite loop
# 	Otherwise if they are in the boss room:
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



