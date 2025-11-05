# BHR 2nd maze generator
import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Generator")

# Global variables for player position
player_x = 0
player_y = 0

# Maze size (will be set by the player)
maze_width = 10
maze_height = 10
grid_size = 10

# Maze grid (0 = empty, 1 = wall)
maze = []

# Ask player for maze size
maze_width = int(input("How wide do you want the maze to be? "))
maze_height = int(input("How tall do you want the maze to be? "))

# Function to create a random maze
def generate_maze():
    global maze
    maze = []
    for y in range(maze_height):
        row = []
        for x in range(maze_width):
            if random.random() < 0.2:  # 20% chance of a wall
                row.append(1)
            else:
                row.append(0)
        maze.append(row)

# Function to draw the maze
def draw_maze():
    turtle.clear()
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    for y in range(maze_height):
        for x in range(maze_width):
            t.goto(x * grid_size - (maze_width * grid_size)//2, 
                   y * grid_size - (maze_height * grid_size)//2)
            if maze[y][x] == 1:
                t.dot(grid_size, "black")
    # Draw player
    t.goto(player_x * grid_size - (maze_width * grid_size)//2, 
           player_y * grid_size - (maze_height * grid_size)//2)
    t.dot(grid_size, "blue")

# Movement functions
def move_up():
    global player_y
    if player_y < maze_height - 1 and maze[player_y + 1][player_x] == 0:
        player_y += 1
        check_finish()
    draw_maze()

def move_down():
    global player_y
    if player_y > 0 and maze[player_y - 1][player_x] == 0:
        player_y -= 1
        check_finish()
    draw_maze()

def move_left():
    global player_x
    if player_x > 0 and maze[player_y][player_x - 1] == 0:
        player_x -= 1
        check_finish()
    draw_maze()

def move_right():
    global player_x
    if player_x < maze_width - 1 and maze[player_y][player_x + 1] == 0:
        player_x += 1
        check_finish()
    draw_maze()

# Check if player reached the goal (top-right corner)
def check_finish():
    global player_x, player_y
    if player_x == maze_width - 1 and player_y == maze_height - 1:
        player_x = 0
        player_y = 0
        generate_maze()

# Set up key bindings
wn.listen()
wn.onkey(move_up, "w")
wn.onkey(move_down, "s")
wn.onkey(move_left, "a")
wn.onkey(move_right, "d")

# Initialize
generate_maze()
draw_maze()
wn.mainloop()
