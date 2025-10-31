# BHR 2nd maze generator
import turtle
import random
bob = turtle.Turtle()
a = random.randint(1,2)
b = 3
maze_grid = [[a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, b]]
def maze_maker(maze_grid, bob):
    x = 1
    for maze_part in maze_grid:
        for maze_piece in maze_part:
            maze_piece = random.randint(1,2)
            if maze_piece == 1:
                turtle.pendown()
                turtle.forward(10)
            else:
                turtle.penup()
                turtle.forward(10)
        turtle.pendown()
        if maze_part == maze_grid[-1]:
            x = 0
        if x == 1:
            turtle.left(90)
            turtle.forward(10)
            turtle.left(90)
            x += 1
        elif x == 2:
            turtle.right(90)
            turtle.forward(10)
            turtle.right(90)
            x -= 1
maze_maker(maze_grid, bob)
turtle.done()

