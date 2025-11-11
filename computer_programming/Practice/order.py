#BHR 2nd order up

#set up the menu
menu = {
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
        "Dihydrogen monoxide": 1000,
        "": 0
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
    #if everything is fine, then give the cost
    return cost





