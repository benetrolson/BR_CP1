import random

# -----------------------------
# Set the player stats in a definition:
# -----------------------------
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
    # Current health
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
        # Unequipped:
        "unequipped": [],
    },
    # Health potions: 0
    "health_potions": 0,
    # Necklace: whichever necklace they have equipped
    "necklace": "",
    # Location: Beginning
    "location": "beginning"
}

weapons = {
    # Weapon name: damage and cooldown
    "beak": {"dmg": 1, "cooldown": 0},
    "sword": {"dmg": 5, "cooldown": 2},
    "axe": {"dmg": 6, "cooldown": 4},
    "spear": {"dmg": 3, "cooldown": 1},
    "club": {"dmg": 4, "cooldown": 3},
    "health_potion": {"heal": 10, "cooldown": 0},
    "health_necklace": {"bonus": 20, "type": "health"},
    "strength_necklace": {"bonus": 20, "type": "strength"},
    "intelligence_necklace": {"bonus": 20, "type": "intelligence"},
    "super_necklace": {"bonus": 20, "type": "all"}
}

enemies_template = {
    # Kid's stats
    "kid": {
        # Weapon 1
        "weapon1": "sword",
        # Health is 20
        "health": 20,
        # Strength is 20
        "strength": 20
    },
    # Adult's stats
    "adult": {
        # Weapon 1
        "weapon1": "sword",
        # Weapon 2
        "weapon2": "axe",
        # Health is 40
        "health": 40,
        # Strength is 40
        "strength": 40
    },
    # Old's stats
    "old": {
        # Weapon 1
        "weapon1": "sword",
        # Weapon 2
        "weapon2": "axe",
        # Weapon 3
        "weapon3": "spear",
        # Health is 20
        "health": 20,
        # Strength is 50
        "strength": 50
    },
    # Gatekeeper's stats
    "gatekeeper": {
        # Weapon 1
        "weapon1": "axe",
        # Weapon 2
        "weapon2": "club",
        # Weapon 3
        "weapon3": "beak",
        # Health is 50
        "health": 50,
        # Strength is 50
        "strength": 50
    },
    # Boss's stats
    "boss": {
        # Weapon 1
        "weapon1": "axe",
        # Weapon 2
        "weapon2": "club",
        # Weapon 3
        "weapon3": "sword",
        # Weapon 4
        "weapon4": "spear",
        # Weapon 5
        "weapon5": "beak",
        # Health is 60
        "health": 60,
        # Strength is 60
        "strength": 60
    }
}

rooms = {
    "beginning": {
        "possible_moves": ["bob", "tutorial"],
        "visited": False,
        "description1": "You return to the place where you woke up. You look around, remembering that the omnipotent and omniscient chickens have sent you down with a purpose, to destroy Earth.",
        "description2": "You are back at the beginning."
    },
    "tutorial": {
        "possible_moves": ["beginning", "bob", "gladiator_ring", "shop"],
        "visited": False,
        "enemy": "kid",
        "description1": "You enter a room with a kid in the center. The kid runs up at you and starts attacking you. Prepare for combat.",
        "description2": "You enter a room with a dead kid in the center. You see the spilled blood on the floor."
    },
    "bob": {
        "possible_moves": ["beginning", "tutorial", "boss_room"],
        "visited": False,
        "necklaces_taken": [],
        "description1": "A chicken sits there, fingering his sword. He waits for you to approach him, holding some necklaces.",
        "description2": "Bob sits there, waiting for you to approach him."
    },
    "gladiator_ring": {
        "possible_moves": ["tutorial", "shop", "mage", "bonus_area_1", "bonus_area_2"],
        "visited": False,
        "description1": "A chicken with a boisterous voice welcomes you to his arena, seeking entertainment.",
        "description2": "The man asks you whether you want to fight another family member or leave."
    },
    "shop": {
        "possible_moves": ["bob", "tutorial", "gladiator_ring", "mage"],
        "visited": False,
        "description": "You find a strange chicken with a bunch of weapons. She awaits your approach."
    },
    "mage": {
        "possible_moves": ["gladiator_ring", "shop", "gatekeeper"],
        "visited": False,
        "boost_given": False,
        "description1": "A floating chicken stands in the center of the room, walking around.",
        "description2": "The mage waits while floating at the top of the room."
    },
    "gatekeeper": {
        "possible_moves": ["shop", "mage", "resting_place"],
        "visited": False,
        "enemy": "gatekeeper",
        "description1": "A chicken floats up and flies towards you.",
        "description2": "The gatekeeper lies on the ground, dead."
    },
    "resting_place": {
        "possible_moves": ["gatekeeper", "boss_room"],
        "visited": False,
        "item": "health_potion",
        "description1": "You see a health potion on the ground.",
        "description2": "You see the way that you should go; forward."
    },
    "boss_room": {
        "possible_moves": ["bob", "gatekeeper"],
        "visited": False,
        "enemy": "boss",
        "description1": "A door slams behind you, locking you into the room. The Chickens look at you, seeming prepared."
    },
    "bonus_area_1": {
        "possible_moves": ["gladiator_ring"],
        "visited": False,
        "necklaces_taken": [],
        "description1": "You see the great and glorious Bob again, waiting with his necklaces.",
        "description2": "Bob, bored, asks why you are here and to shut the nonexistent door on the way out."
    },
    "bonus_area_2": {
        "possible_moves": ["gladiator_ring", "beginning"],
        "visited": False,
        "description1": "Bob welcomes you and gives you a weird necklace after taking yours.",
        "description2": "Bob greets you with a cheerful 'SHUT THE (nonexistent) DOOR ON YOUR WAY OUT!'"
    }
}

dialogue = {
    "bob": [],
    "mage": [],
    "shop": [],
    "tutorial": [],
    "gladiator_ring": [],
    "gatekeeper": [],
    "resting_place": [],
    "boss_room": []
}

def combat(enemy_name, player_stats):
    # Get enemy from template
    enemy = enemies_template[enemy_name].copy()
    # Initialize enemy weapon cooldowns
    enemy_cooldowns = {}
    for w in enemy:
        if "weapon" in w:
            enemy_cooldowns[w] = 0
    messages = []
    # Determine whose turn it is: 0=enemy, 1=player
    turn = 0
    while enemy["health"] > 0 and player_stats["current_health"] > 0:
        if turn == 0:
            # Get usable weapons
            usable_weapons = [w for w in enemy_cooldowns if enemy_cooldowns[w] == 0]
            
            if not usable_weapons:
                messages.append("Enemy has no usable weapons this turn.")
            else:
                # Infinite loop until valid weapon chosen
                while True:
                    weapon_choice = random.choice(usable_weapons)
                    dmg = ((enemy["strength"] / 100) + 1) * weapons[enemy[weapon_choice]]["dmg"]
                    player_stats["current_health"] -= dmg
                    messages.append(f"Enemy used {weapon_choice} and dealt {dmg:.1f} damage!")
                    # Set cooldown for that weapon
                    enemy_cooldowns[weapon_choice] = weapons[enemy[weapon_choice]]["cooldown"]
                    break
            # Reduce all other cooldowns by 1
            for w in enemy_cooldowns:
                if enemy_cooldowns[w] > 0 and w != weapon_choice:
                    enemy_cooldowns[w] -= 1
            turn = 1
        else:
            options = []
            # Check usable weapons
            for w in player_stats["weapons"]["equipped"]:
                if player_stats["weapons"]["equipped"][w] == 0:
                    options.append(w)
            # Check if health potion is available
            if player_stats["health_potions"] > 0:
                options.append("health_potion")
            # Display options as numbers
            print("Choose an action (number):")
            for i, option in enumerate(options):
                print(f"{i+1}: {option}")
            choice = int(input("> ")) - 1
            selected = options[choice]
            if selected == "health_potion":
                # Use health potion
                player_stats["current_health"] += weapons["health_potion"]["heal"]
                player_stats["health_potions"] -= 1
                messages.append("You used a health potion (+10 HP).")
            else:
                # Attack with weapon
                dmg = ((player_stats["stats"]["strength"] / 100) + 1) * weapons[selected]["dmg"]
                enemy["health"] -= dmg
                messages.append(f"You used {selected} and dealt {dmg:.1f} damage!")
                # Set cooldown for used weapon
                player_stats["weapons"]["equipped"][selected] = weapons[selected]["cooldown"]
            # Reduce all other cooldowns by 1
            for w in player_stats["weapons"]["equipped"]:
                if player_stats["weapons"]["equipped"][w] > 0 and w != selected:
                    player_stats["weapons"]["equipped"][w] -= 1
            turn = 0
    return messages

# -----------------------------
# Movement function
# -----------------------------
def move(current_room, target_room):
    if target_room in rooms[current_room]["possible_moves"]:
        player_stats["location"] = target_room
        if not rooms[target_room]["visited"]:
            print(rooms[target_room].get("description1", ""))
            rooms[target_room]["visited"] = True
        else:
            print(rooms[target_room].get("description2", ""))
    else:
        print("Cannot move there!")

# -----------------------------
# Mage interaction
# -----------------------------
def mage_interaction():
    if not rooms["mage"]["boost_given"]:
        print("Choose a stat to boost (1-Int, 2-Str, 3-Health):")
        choice = int(input("> "))
        if choice == 1:
            player_stats["stats"]["intelligence"] += 10
        elif choice == 2:
            player_stats["stats"]["strength"] += 10
        else:
            player_stats["stats"]["health"] += 10
        rooms["mage"]["boost_given"] = True

# -----------------------------
# Shop function
# -----------------------------
def shop_interaction():
    print("Welcome to the shop! Exchange weapons for health potions.")
    print("Your weapons:")
    for i, w in enumerate(player_stats["weapons"]["unequipped"]):
        print(f"{i+1}: {w}")
    choice = int(input("> ")) - 1
    if 0 <= choice < len(player_stats["weapons"]["unequipped"]):
        weapon = player_stats["weapons"]["unequipped"].pop(choice)
        player_stats["health_potions"] += 1
        print(f"Traded {weapon} for a health potion.")

# -----------------------------
# Main game loop
# -----------------------------
while True:
    print("Welcome to the game!")
    # Give sword at start
    take_sword = input("Do you want to take the sword? (1-Yes, 2-No) ")
    if take_sword == "1":
        player_stats["weapons"]["equipped"]["weapon1"] = 0
        print("You picked up the sword!")
        break

# Infinite game loop
while True:
    print(f"Current location: {player_stats['location']}")
    # Show possible moves
    options = rooms[player_stats["location"]]["possible_moves"]
    for i, r in enumerate(options):
        print(f"{i+1}: {r}")
    choice = int(input("> ")) - 1
    if 0 <= choice < len(options):
        move(player_stats["location"], options[choice])
        loc = player_stats["location"]
        # If combat room
        if "enemy" in rooms[loc]:
            msgs = combat(rooms[loc]["enemy"], player_stats)
            for m in msgs:
                print(m)
        # If mage room
        if loc == "mage":
            mage_interaction()
        # If shop
        if loc == "shop":
            shop_interaction()
    else:
        print("Invalid choice!")

    # Check for end of game
    if loc == "boss_room" and player_stats["current_health"] > 0:
        print("Congratulations! You completed the game.")
        play_again = input("Play again? (1-Yes, 2-No) ")
        if play_again == "2":
            break
        else:
            # Reset game
            player_stats["current_health"] = 50
            player_stats["location"] = "beginning"
            for room in rooms:
                rooms[room]["visited"] = False
