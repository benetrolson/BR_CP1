# BHR 2nd turtle race
import turtle 
import random 
patience = 0
money = 500
def setup():
    for turtle in turtles:
        turtle.speed(0)
    for turtle in turtles:
        turtle.shape("turtle")
    turtle1.color("blue") 
    turtle2.color("teal") 
    turtle3.color("green") 
    turtle4.color("orange") 
    turtle5.color("red")  
    turtle1.teleport(-500, 40)
    turtle2.teleport(-500, 20) 
    turtle3.teleport(-500, 0) 
    turtle4.teleport(-500, -20) 
    turtle5.teleport(-500, -40) 
def move():
    while True:
        for turtle in turtles:
            turtle.forward(random.randint(-10,100) / 10)
            turtle2.forward(0.1)
            turtle5.backward(0.1)
def winner():
    if turtle1.xcor() >= 500 and "1" not in finish_order:
        turtle1.forward(50) 
        finish_order.append("1")
        turtle1.teleport(-1000, 1000)
        turtle1.clear()
    if turtle2.xcor() >= 500 and "2" not in finish_order:
        turtle2.forward(50) 
        finish_order.append("2")
        turtle2.teleport(-1000, 1000)
        turtle2.clear()
    if turtle3.xcor() >= 500 and "3" not in finish_order:
        turtle3.forward(50) 
        finish_order.append("3")
        turtle3.teleport(-1000, 1000)
        turtle3.clear()
    if turtle4.xcor() >= 500 and "4" not in finish_order:
        turtle4.forward(50) 
        finish_order.append("4")
        turtle4.teleport(-1000, 1000)
        turtle4.clear()
    if turtle5.xcor() >= 500 and "5" not in finish_order:
        turtle5.forward(50) 
        finish_order.append("5")
        turtle5.teleport(-1000, 1000)
        turtle5.clear()
drawer = turtle.Turtle()
turtle1 = turtle.Turtle() 
turtle2 = turtle.Turtle() 
turtle3 = turtle.Turtle() 
turtle4 = turtle.Turtle() 
turtle5 = turtle.Turtle() 
drawer.color("black")
drawer.speed(0)
drawer.teleport(510, 500)
drawer.right(90)
for i in range(50):
    drawer.begin_fill()
    for x in range(5):
        drawer.forward(10)
        drawer.right(90)
    drawer.end_fill()
    drawer.left(90)
    drawer.begin_fill()
    for x in range(5):
        drawer.forward(10)
        drawer.left(90)
    drawer.end_fill()
    drawer.right(90)
drawer.hideturtle()
while True:
    finish_order = []
    turtles = [turtle1, turtle2, turtle3, turtle4, turtle5]
    setup()
    print(f"You have ${money}. ")
    bet_choice = input("Which turtle do you want to bet on? If you don't want to bet on any, write anything. Blue(1), teal(2), green(3), orange(4), red(5). ")
    if bet_choice in ["1", "2", "3", "4", "5"]:
        while True:
            bet_amount = input("How much do you want to bet on this turtle? ")
            if bet_amount.isdigit():
                bet_amount = int(bet_amount)
            else:
                print("That is an invalid input. Please try again. ")
                continue
            if money < bet_amount or bet_amount <= 0:
                print("That is an invalid input. Please try again. ")
            else:
                break
    else:
        bet_amount = 0
        move()
        winner()
        if len(finish_order) == 5:
            break
    if finish_order[0] == bet_choice:
        bet_amount *= 4
        money += bet_amount
        print("Your turtle finished in 1st place! ")
    elif finish_order[1] == bet_choice:
        money += bet_amount
        print("Your turtle finished in 2nd place! ")
    elif finish_order[2] == bet_choice:
        print("Your turtle finished in 3rd place! ")
    elif finish_order[3] == bet_choice:
        money -= bet_amount
        print("Your turtle finished in 4th place! ")
    elif finish_order[4] == bet_choice:
        print("Your turtle finished in last place! ")
        bet_choice *= 2
        money -= bet_amount
    else:
        print("You chose not to bet this round. ")
    if money <= 0 and patience <= 5:
        print("Here is some pity money. I felt sorry for you. ")
        money = 1000
        patience += 1
    if patience >= 5:
        print("JK. You asked for too much money! I'm not giving any money to you! You are being kicked out! ")
        break
