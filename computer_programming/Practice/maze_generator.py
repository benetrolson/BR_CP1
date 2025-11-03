# BHR 2nd maze generator
import turtle
import random
bob = turtle.Turtle()
a = random.randint(1,2)
b = 3
rows = [[a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a]]
columns = [[a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a], [a, a, a, a, a, a, a, a]]

def randomizer(rows, columns):
    for row in rows:
        if row != rows.
        for piece in row:
            piece = random.randint(0, 1)
            row.pop()
            row.append(piece)
        rows.pop()
        row.append(row)
    for column in columns:
        for piece in column:
            piece = random.randint(0, 1)
            column.pop()
            column.append(piece)
        columns.pop()
        columns.append(column)
    return(rows, columns)

def maze_checker():
    while True:
        rows, columns = randomizer(rows, columns)
        row_size = len(rows) - 1
        column_size = len(rows) - 1
        visited = []
        stack = [(0, 0)]
        while stack:
            x, y = stack.pop()
            if x == row_size - 1 and y == column_size - 1:
                return rows, columns
            if (x, y) in visited:
                continue
            visited.add(x, y)
            if x < row_size -1 and columns[y][x+1] == 0:
                stack.append(x+1, y)
            if y < column_size -1 and rows[x][y+1] == 0:
                stack.append(x, y+1)
            if x > 0 and columns[y][x+1] == 0:
                stack.append(x-1, y)
            if y > 0 and rows[x][y+1] == 0:
                stack.append(x, y-1)

def maze_maker(rows, columns):
    x = 1
    for row in rows:
        for piece in row:
            if piece == 1:
                turtle.pendown()
                turtle.forward(10)
            else:
                turtle.penup()
                turtle.forward(10)
        turtle.pendown()
        if row == rows[-1]:
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
maze_maker(rows, columns)
turtle.done()

