#BHR 2nd drawing starter
import turtle

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length/3)
            turtle.backward(length)
            turtle.right(60)

turtle.Turtle
turtle.speed(0)
turtle.color("blue")
turtle.teleport(0, 0)

for i in range(6):
    draw_branch(100)
    turtle.right(60)

turtle.hideturtle()
turtle.done()


