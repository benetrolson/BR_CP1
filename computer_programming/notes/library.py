#BHR 2nd library notes
import random
import turtle
number = random.randint(100, 500)
length = 10
turn = 90
turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.pensize(1)
turtle.shape("turtle")
turtle.speed(10000000)
while True:
    turtle.color("teal")
    for x in range(4):
        turtle.forward(length)
        turtle.right(turn)
    turtle.color("blue")
    for x in range(4):
        turtle.forward(length)
        turtle.left(turn)
    turtle.color("#19A0DF")
    for x in range(4):
        turtle.right(turn)
        turtle.forward(length)
    turtle.color("#0CE793")
    for x in range(4):
        turtle.left(turn)
        turtle.forward(length)
    length += 2.5
    turn += 0.001

turtle.done()


