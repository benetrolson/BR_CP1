# BHR 2nd maze generator
import turtle
import random
bob = turtle.Turtle()
a = random.randint(0,2)
b = 3

def randomizer():
    rows = [[a, b, a, a, a, a, a], 
            [b, a, a, a, a, a, a], 
            [b, a, a, a, a, a, a], 
            [b, a, a, a, a, a, a], 
            [b, a, a, a, a, a, a], 
            [a, a, a, a, a, a, a]]
    new_rows = []
    new_columns = []
    new_row = []
    new_column = []
    for row in rows:
        for i in row:
            if i == 0:
                wall = random.randint(1,2)
                new_row.append(wall)
                new_column.append(wall)
            else:
                row_wall = random.choice([0, 0, 1])
                new_row.append(row_wall)
                column_wall = random.choice([0, 0, 0, 1])
                new_column.append(column_wall)
        new_rows.append(new_row)
        new_row = []
        new_columns.append(new_column)
        new_column = []
    return(new_rows, new_columns)

def maze_checker():
    while True:
        rows, columns = randomizer()
        row_size = len(rows)
        column_size = len(rows[0])
        visited = set()
        stack = [(0, 0)]
        while True:
            if stack == []:
                break
            x, y = stack.pop()
            if x == row_size - 1 and y == column_size - 1:
                return rows, columns
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if x + 1 < column_size and y < len(columns) and x < len(columns[y]) and columns[y][x] != 1:#right
                stack.append(((x+1), y))
            if y - 1 >= 0 and x < len(rows[y-1]) and rows[y-1][x] != 1:#up
                stack.append((x, (y-1)))
            if x - 1 >= 0 and y < len(columns) and x - 1 < len(columns[y]) and columns[y][x-1] != 1:#left
                stack.append(((x-1), y))
            if y + 1 < row_size and x < len(rows[y]) and rows[y][x] != 1:#down
                stack.append((x, (y+1)))

def maze_maker(bob):
    x = 20
    y = 20
    bob.teleport(20, 0)
    bob.forward(120)
    bob.teleport(0,0)
    bob.setheading(90)
    bob.forward(140)
    bob.setheading(0)
    rows, columns = maze_checker()
    bob.teleport(0, y)
    y += 20
    for row in rows:
        for piece in row:
            if piece == 1:
                bob.pendown()
                bob.forward(20)
            else:
                bob.penup()
                bob.forward(20)
        bob.teleport(0, y)
        y += 20
    bob.pendown()
    bob.forward(120)
    bob.teleport(0,0)
    bob.setheading(90)
    bob.teleport(x, 0)
    x += 20
    for column in columns:
        for piece in column:
            if piece == 1:
                bob.pendown()
                bob.forward(20)
            else:
                bob.penup()
                bob.forward(20)
        bob.teleport(x, 0)
        x += 20
    bob.pendown()
    bob.forward(140)
    bob.hideturtle()
maze_maker(bob)
turtle.done()
