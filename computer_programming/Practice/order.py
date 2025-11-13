#BHR 2nd order up
import random
side_choices = []
#set up the menu
menu_1 = {
    "main": {
        "Chocolate Ice Cream": 5,
        "Vanilla Ice Cream": 5,
        "Strawberry Ice Cream": 10,
        "Neapolitan Ice Cream": 10,
        "Nutella Ice Cream": 15,
        "Cake Ice Cream": 15, 
        "": 0
    }, 
    "side": {
        "French Fries": 1, 
        "Potato Salad": 2,
        "Fried Crickets": 2, #I've had these before, so you can't say that this is not a feasible food. 
        "Chocolate Chips": 3,
        "Cake": 10, 
        "": 0
    },
    "drink": {
        "Amazon Water": 50, 
        "Indian Ocean Water": 50,
        "Filtered Human Blood": 500,
        "Melted Gold": -20,#No takeout
        "Human Sweat": 2,
        "Dihydrogen Monoxide": 1000,
        "": 0
    }
}
menu_2 = {
    "main": {
        "1": "Chocolate Ice Cream",
        "2": "Vanilla Ice Cream",
        "3": "Strawberry Ice Cream",
        "4": "Neapolitan Ice Cream",
        "5": "Nutella Ice Cream",
        "6": "Cake Ice Cream", 
        "": 0
    }, 
    "side": {
        "1": "French Fries", 
        "2": "Potato Salad",
        "3": "Fried Crickets", #I've had these before, so you can't say that this is not a feasible food. 
        "4": "Chocolate Chips",
        "5": "Cake", 
        "": 0
    },
    "drink": {
        "1": "Amazon Water", 
        "2": "Indian Ocean Water",
        "3": "Filtered Human Blood",
        "4": "Human Sweat",
        "5": "Dihydrogen Monoxide",
        "6": "Melted Gold",#No takeout
        "": 0
    }
    }

#set up the function to check the menu 
def validation(dictionary, dictionary2, main_choice, some_side_choices, drink_choice):
    #reset cost
    cost = 0
    if main_choice in dictionary2["main"]:
        main_choice = dictionary2["main"]
    for side_choice in some_side_choices:
        if side_choice in dictionary2["side"]:
            side_choice = dictionary2["side"]
            side_choices.append(dictionary2["side"])
    if drink_choice in dictionary2["drink"]:
        drink_choice = dictionary2["drink"]
    #check if the menu choice is in the menu main dishes
    if main_choice in dictionary["main"]:
        #add the price
        cost += dictionary["main"][main_choice]
    #otherwise
    else:
        #return false
        return False
    for side_choice in side_choices:
        #check if the side choice is in the menu side dishes
        if side_choice in dictionary["side"]:
            #add the price
            cost += dictionary["side"][side_choice]
        #otherwise
        else:
            #return false
            return False
    #do the same for the drink
    if drink_choice in dictionary["drink"]:
        #add the price
        cost += dictionary["drink"][drink_choice]
    #otherwise
    else:
        #return false
        return False
    #do a forced tip
    cost *= random.randint(2, 10)
    #add tax
    cost *= (1 + (random.randint(1, 9) / 10))
    #if everything is fine, then give the cost
    return cost

#infinite loop
while True:
    #check what they want for their main food
    main_choice = input("What do you want for your main meal? Chocolate Ice Cream(1), Vanilla Ice Cream(2), Strawberry Ice Cream(3), Neapolitan Ice Cream(4), Nutella Ice Cream(5), Cake Ice Cream(6). ").title().strip()
    #check what they want for their side
    side_choice = input("What do you want for your side? French fries(1), Potato salad(2), Fried crickets(3), Chocolate chips(4), Cake(5). ").title().strip()
    side_choices.append(side_choice)
    #check what they want for their side
    side_choice = input("What do you want for your side? French fries(1), Potato salad(2), Fried crickets(3), Chocolate chips(4), Cake(5). ").title().strip()
    side_choices.append(side_choice)
    #check what they want for their drink
    drink_choice = input("What do you want for your drink? Amazon water(1), Indian Ocean water(2), Filtered human blood(3), Human sweat(4), Dihydrogen monoxide(5). ").title().strip()
    #check if they want to revise their order
    check = input("Do you want to revise your order? If so, please answer 'yes'. ").strip().lower()
    #if they do
    if check == "yes":
        #restart the loop
        continue
    #run the function
    cost, main_choice, side_choices, drink_choice = validation(menu_1, menu_2, main_choice, side_choices, drink_choice)
    if cost != False:
    #display the order and the bill
        check = input(f"You ordered {main_choice}, {side_choices[0]}, {side_choices[1]}, and {drink_choice}. Your bill is {cost} with a tip. ")
        side_choices = []
        #if their drink is gold
        if drink_choice == "Melted Gold" or drink_choice == "6":
            #they wake up in a hospital, their throat scalded and a surgery preformed to remove the gold
            check = input("You wake up in a hospital with your throat scalded and a pain in your stomach. You then learn that the hospital had preformed surgery to get the gold out of you. Your tongue was disentagrated in the first few seconds of drinking the gold, and now you will have to eat and drink through those tube things. ")
    else:
        print("You did not order succesfuly. ")
