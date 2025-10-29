# BHR 2nd turtle race
import turtle 
import random 
money = 500
bet_choice = input("Which turtle do you want to bet on? If you don't want to bet on any, write anything. Blue(1), teal(2), green(3), orange(4), red(5). ")
if bet_choice == "1" or "2" or "3" or "4" or "5":
    print(f"You have ${money}. ")
    bet_amount = input("How much do you want to bet on this turtle? ")
    #if money <= bet_amount:
        
drawer = turtle.Turtle()
turtle1 = turtle.Turtle() 
turtle2 = turtle.Turtle() 
turtle3 = turtle.Turtle() 
turtle4 = turtle.Turtle() 
turtle5 = turtle.Turtle() 
turtle1.speed(0)
turtle2.speed(0) 
turtle3.speed(0) 
turtle4.speed(0) 
turtle5.speed(0) 
drawer.speed(1000000000)
turtle1.shape("turtle") 
turtle2.shape("turtle") 
turtle3.shape("turtle") 
turtle4.shape("turtle") 
turtle5.shape("turtle")  
turtle1.color("blue") 
turtle2.color("teal") 
turtle3.color("green") 
turtle4.color("orange") 
turtle5.color("red")  
drawer.color("black")
turtle1.teleport(-500, 40)
turtle2.teleport(-500, 20) 
turtle3.teleport(-500, 0) 
turtle4.teleport(-500, -20) 
turtle5.teleport(-500, -40) 
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
drawer.penup()
while True:
    turtle1.forward(random.randint(1,100) / 10) 
    turtle2.forward(random.randint(1,100) / 10) 
    turtle3.forward(random.randint(1,100) / 10) 
    turtle4.forward(random.randint(1,100) / 10) 
    turtle5.forward(random.randint(1,100) / 10) 
    if turtle1.xcor() >= 500:
        turtle1.forward(30) 
        print("Blue turtle wins! ")
        break
    elif turtle2.xcor() >= 500:
        turtle2.forward(30) 
        print("Teal turtle wins! ")
        break
    elif turtle3.xcor() >= 500:
        turtle3.forward(30) 
        print("Green turtle wins! ")
        break
    elif turtle4.xcor() >= 500:
        turtle4.forward(30) 
        print("Orange turtle wins! ")
        break
    elif turtle5.xcor() >= 500:
        turtle5.forward(30) 
        print("Red turtle wins! ")
        break

