# BHR 2nd maze generator
import turtle
import random
bob = turtle.Turtle()
a = random.randint(0,2)
b = 3

def randomizer():
    rows = [[a, a, a, a, a, a], [a, a, a, a, a, a], [a, a, a, a, a, a], [a, a, a, a, a, a],[a, a, a, a, a, a], [a, a, a, a, a, a]]
    columns = [[a, a, a, a, a, a], [a, a, a, a, a, a], [a, a, a, a, a, a], [a, a, a, a, a, a],[a, a, a, a, a, a], [a, a, a, a, a, a]]
    new_rows = []
    new_columns = []
    new_row = []
    new_column = []
    for row in rows:
        for i in row:
            wall = random.randint(0, 1)
            new_row.append(wall)
        new_rows.append(new_row)
    for column in columns:
        for i in column:
            wall = random.randint(0, 1)
            new_column.append(wall)
        new_columns.append(new_column)
    return(new_rows, new_columns)

def maze_checker():
    while True:
        rows, columns = randomizer()
        row_size = len(rows) - 1
        column_size = len(rows) - 1
        visited = []
        stack = [(0, 0)]
        while True:
            if stack == []:
                break
            x, y = stack.pop()
            if x == row_size - 1 and y == column_size - 1:
                return rows, columns
            if (x, y) in visited:
                continue
            visited.append((x, y))
            if x < row_size -1 and columns[y][x+1] == 0:#right
                stack.append(((x+1), y))
            if y < column_size -1 and rows[x][y+1] == 0:#up
                stack.append((x, (y+1)))
            if x > 0 and columns[y][x+1] == 0:#left
                stack.append(((x-1), y))
            if y > 0 and rows[x][y+1] == 0:#down
                stack.append((x, (y-1)))

def maze_maker(bob):
    x = 1
    rows, columns = maze_checker()
    for row in rows:
        for piece in row:
            if piece != 0:
                bob.pendown()
                bob.forward(10)
            else:
                bob.penup()
                bob.forward(10)
        bob.pendown()#teleport the turtle to the left side so that the turtle doesn't reverse the order
        if x == 1:
            bob.left(90)
            bob.pendown()
            bob.backward(10)
            bob.forward(20)
            bob.left(90)
            x = 2
        elif x == 2:
            bob.right(90)
            bob.pendown()
            bob.backward(10)
            bob.forward(20)
            bob.right(90)
            x = 1
    bob.teleport(0,0)
    bob.left(90)
    for column in columns:
        for piece in column:
            if piece != 0:
                bob.pendown()
                bob.forward(10)
            else:
                bob.penup()
                bob.forward(10)
        bob.pendown()
        if column == columns[-1][-1]:
            x = 0
        if x == 1:
            bob.right(90)
            bob.pendown()
            bob.backward(10)
            bob.forward(20)
            bob.right(90)
            x += 1
        elif x == 2:
            bob.left(90)
            bob.pendown()
            bob.backward(10)
            bob.forward(20)
            bob.left(90)
            x -= 1
maze_maker(bob)
turtle.done()

