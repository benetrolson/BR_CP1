#BHR 2nd order up

#set up the menu
menu = {
    "main": {
        "chocolate ice cream": 5,
        "vanilla ice cream": 5,
        "strawberry ice cream": 10,
        "neapolitan ice cream": 10,
        "nutella ice cream": 15,
        "cake ice cream": 15,
        "none": 0
    }, 
    "side": {
        "french fries": 1, 
        "potato salad": 2,
        "fried crickets": 2, #I've had these before, so you can't say that this is not a feasible food. 
        "chocolate chips": 3,
        "cake": 10,
        "none": 0
    },
    "drink": {
        "Amazon water": 50, 
        "Indian Ocean water": 50,
        "filtered human blood": 500,
        "melted gold": -20,#No takeout
        "human sweat": 2,
        "none": 0
    }
}

#set up the function to check the menu 
def validation(dictionary, menu_choice, side_choice, drink_choice):
    #reset cost
    cost = 0
    #check if the menu choice is in the menu main dishes
    if menu_choice in dictionary["main"]:
        #add the price
        cost += dictionary["main"][menu_choice]
    #otherwise
    else:
        #return false
        return False
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





