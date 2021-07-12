import turtle
import math
import random

# - Setup the turtle window
turtle.setup(800, 700)
turtle.title("Pacman Game")
turtle.bgcolor("black")

# - Setup the turtle
turtle.speed(0)
turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# - Define the game timing (30 frames per second)
frame_time = 1000 // 30

# - Define the maze information
maze_x       = -300
maze_y       = -270
maze_columns = 21
maze_rows    = 19

# - Define the tile information
tile_size = 30

# - Define the food information
food_size  = 10
food_count = 0

# - Define the pacman information
pacman_size  = 30
pacman_speed = 6
pacman_x     = 0
pacman_y     = 0

# - Create the variables for the pacman movement
current_move = ""   # This is the current movement
next_move = ""      # This is the next movement

# - Define all ghost information
ghost_size = 30
ghost_speed = 6
ghost_start_x = 0
ghost_start_y = 0
ghost_x_1 = 0
ghost_y_1 = 0
ghost_x_2 = 0
ghost_y_2 = 0
ghost_x_3 = 0
ghost_y_3 = 0
ghost_x_4 = 0
ghost_y_4 = 0
ghosts = []

# - Maze of the game
#   + : wall
#   . : food
#   o : power food
#   P : starting position of pacman
#   G : starting position of ghosts
maze = [
    #012345678901234567890 - total 21 columns
    "+++ +++++ +++++++++++", # 0
    "+........   .......o+", # 1
    "+...+++..+....+...+.+", # 2
    "+..+...+.++.+.+...+.+", # 3
    "+.++.o.....+..+++++.+", # 4
    "+..+...+.+......+...+", # 5
    "+...+++....++..o+ ..+", # 6
    "+...... ...o   ...o.+", # 7
    "+++.+++++++++++++..++", # 8
    "  .................  ", # 9
    "+++.++++++G++++++ +++", # 10
    "+...................+", # 11
    "+.+...+.+++++.+...+.+", # 12
    "+.+.o.+...+...+...+.+", # 13
    "+.+++++...+...+++++.+", # 14
    "+...+.....+...+.o.+.+", # 15
    "+...+...+++++.+...+.+", # 16
    "+.........P....o....+", # 17
    "+++ +++++ +++++++++++"  # 18 - total 19 rows
]


# - Draw the maze
for i in range(maze_columns):
    for j in range(maze_rows):
        # Get the tile
        tile = maze[j][i]
        
        # - Find and put turtle to the x, y position of the tile 
        tile_x= maze_x+ i*tile_size
        tile_y= maze_y +(maze_rows- j- 1)*tile_size
        turtle.goto(tile_x, tile_y)
        
        # - Draw the tiles for walls, food and power food
        if tile== "+":
            turtle.shape("square")
            turtle.color("blue", "black")
            turtle.shapesize(tile_size/20, tile_size/20, 1)
            turtle.begin_fill()
            turtle.stamp()
            turtle.end_fill()
        elif tile== ".":
            turtle.color("yellow", "yellow")
            turtle.begin_fill()
            turtle.dot(food_size/2)
            turtle.end_fill()
            food_count += 1
        elif tile== "o":
            turtle.color("white", "white")
            turtle.begin_fill()
            turtle.dot(food_size)
            turtle.end_fill()
            food_count += 1
        elif tile== "P":
            pacman_x= tile_x
            pacman_y= tile_y
        elif tile== "G":
            ghost_start_x= tile_x
            ghost_start_y= tile_y

# - Create the score
score = 0
turtle_score = turtle.Turtle()
turtle_score.color("white")
turtle_score.hideturtle()
turtle_score.up()
turtle_score.goto(-270, 300)
turtle_score.down()

# - Opening and Closing of Pacman mouth
k = 0
setheading_angle = 0
turtle_fan = turtle.Turtle()
turtle_fan.hideturtle()
turtle_fan.up()
turtle_fan.goto(pacman_x, pacman_y)
turtle_fan.down()
def draw_pacman(x, color):
    global k

    if k % 10 == 0:
        turtle_fan.setheading(x)
        turtle_fan.color(color, color)
        turtle_fan.begin_fill()
        turtle_fan.left(50)
        turtle_fan.forward(pacman_size/2)
        turtle_fan.left(90)
        turtle_fan.circle(pacman_size/2, 260)
        turtle_fan.left(90)
        turtle_fan.forward(pacman_size/2)    
        turtle_fan.end_fill()
        k += 1
    elif k % 10 == 5:
        turtle_fan.setheading(x)
        turtle_fan.up()
        turtle_fan.right(90)
        turtle_fan.forward(pacman_size/2)
        turtle_fan.left(90)
        turtle_fan.down()
        turtle_fan.color(color, color)
        turtle_fan.begin_fill()
        turtle_fan.circle(pacman_size/2) 
        turtle_fan.end_fill()
        k += 1
    elif k % 10 == 1 or k % 10 == 9:
        turtle_fan.setheading(x)
        turtle_fan.color(color, color)
        turtle_fan.begin_fill()
        turtle_fan.left(40)
        turtle_fan.forward(pacman_size/2)
        turtle_fan.left(90)
        turtle_fan.circle(pacman_size/2, 280)
        turtle_fan.left(90)
        turtle_fan.forward(pacman_size/2)    
        turtle_fan.end_fill()
        k += 1
    elif k % 10 == 2 or k % 10 == 8:
        turtle_fan.setheading(x)
        turtle_fan.color(color, color)
        turtle_fan.begin_fill()
        turtle_fan.left(30)
        turtle_fan.forward(pacman_size/2)
        turtle_fan.left(90)
        turtle_fan.circle(pacman_size/2, 300)
        turtle_fan.left(90)
        turtle_fan.forward(pacman_size/2)    
        turtle_fan.end_fill()
        k += 1
    elif k % 10 == 3 or k % 10 == 7:
        turtle_fan.setheading(x)
        turtle_fan.color(color, color)
        turtle_fan.begin_fill()
        turtle_fan.left(20)
        turtle_fan.forward(pacman_size/2)
        turtle_fan.left(90)
        turtle_fan.circle(pacman_size/2, 320)
        turtle_fan.left(90)
        turtle_fan.forward(pacman_size/2)    
        turtle_fan.end_fill()
        k += 1
    elif k % 10 == 4 or k % 10 == 6:
        turtle_fan.setheading(x)
        turtle_fan.color(color, color)
        turtle_fan.begin_fill()
        turtle_fan.left(10)
        turtle_fan.forward(pacman_size/2)
        turtle_fan.left(90)
        turtle_fan.circle(pacman_size/2, 340)
        turtle_fan.left(90)
        turtle_fan.forward(pacman_size/2)    
        turtle_fan.end_fill()
        k += 1

    #print(k)
    #time.sleep(0.5)

# - Create the pacman turtle
turtle_pacman = turtle.Turtle()
turtle_pacman.hideturtle()
turtle_pacman.up()
turtle_pacman.goto(pacman_x, pacman_y)
turtle_pacman.down()

# - Create the ghost turtle 1
turtle_ghost_1 = turtle.Turtle()
turtle_ghost_1.hideturtle()
turtle_ghost_1.up()
turtle_ghost_1.goto(ghost_start_x, ghost_start_y)
turtle_ghost_1.down()
ghost_x_1 = ghost_start_x
ghost_y_1 = ghost_start_y
ghost_1 = {"turtle":turtle_ghost_1, "move":"left"}
ghosts.append(ghost_1)

# - Create ghost face 1
turtle_ghost_face_1 = turtle.Turtle()
turtle_ghost_face_1.hideturtle()
turtle_eyes_1 = turtle.Turtle()
turtle_eyes_1.hideturtle()
def draw_face_of_ghost_1(eyes_angle_1):
    turtle_ghost_face_1.color("red", "red")
    turtle_ghost_face_1.setheading(0)
    turtle_ghost_face_1.up()
    turtle_ghost_face_1.dot(ghost_size)
    turtle_ghost_face_1.up()
    turtle_ghost_face_1.left(90)
    turtle_ghost_face_1.left(55)
    turtle_ghost_face_1.forward(ghost_size/4)
    turtle_ghost_face_1.down()
    turtle_ghost_face_1.dot(ghost_size/2.5, "white")
    turtle_ghost_face_1.up()
    turtle_ghost_face_1.left(180)
    turtle_ghost_face_1.forward(ghost_size/4)
    turtle_ghost_face_1.left(70)
    turtle_ghost_face_1.forward(ghost_size/4)
    turtle_ghost_face_1.dot(ghost_size/2.5, "white")
    turtle_eyes_1.setheading(0)
    turtle_eyes_1.up()
    turtle_eyes_1.left(eyes_angle_1)
    turtle_eyes_1.forward(ghost_size/5)
    turtle_eyes_1.down()
    turtle_eyes_1.setheading(0)
    turtle_eyes_1.up()
    turtle_eyes_1.left(90)
    turtle_eyes_1.left(55)
    turtle_eyes_1.forward(ghost_size/4)
    turtle_eyes_1.down()
    turtle_eyes_1.dot(ghost_size/4, "blue")
    turtle_eyes_1.up()
    turtle_eyes_1.left(180)
    turtle_eyes_1.forward(ghost_size/4)
    turtle_eyes_1.left(70)
    turtle_eyes_1.forward(ghost_size/4)
    turtle_eyes_1.dot(ghost_size/4, "blue")

# - Create the ghost turtle 2
turtle_ghost_2 = turtle.Turtle()
turtle_ghost_2.hideturtle()
turtle_ghost_2.up()
turtle_ghost_2.goto(ghost_start_x, ghost_start_y)
turtle_ghost_2.down()
ghost_x_2 = ghost_start_x
ghost_y_2 = ghost_start_y
ghost_2 = {"turtle":turtle_ghost_2, "move":"left"}
ghosts.append(ghost_2)

# - Create ghost face 2
turtle_ghost_face_2 = turtle.Turtle()
turtle_ghost_face_2.hideturtle()
turtle_eyes_2 = turtle.Turtle()
turtle_eyes_2.hideturtle()
def draw_face_of_ghost_2(eyes_angle_2):
    turtle_ghost_face_2.color("orange", "orange")
    turtle_ghost_face_2.setheading(0)
    turtle_ghost_face_2.up()
    turtle_ghost_face_2.dot(ghost_size)
    turtle_ghost_face_2.up()
    turtle_ghost_face_2.left(90)
    turtle_ghost_face_2.left(55)
    turtle_ghost_face_2.forward(ghost_size/4)
    turtle_ghost_face_2.down()
    turtle_ghost_face_2.dot(ghost_size/2.5, "white")
    turtle_ghost_face_2.up()
    turtle_ghost_face_2.left(180)
    turtle_ghost_face_2.forward(ghost_size/4)
    turtle_ghost_face_2.left(70)
    turtle_ghost_face_2.forward(ghost_size/4)
    turtle_ghost_face_2.dot(ghost_size/2.5, "white")
    turtle_eyes_2.setheading(0)
    turtle_eyes_2.up()
    turtle_eyes_2.left(eyes_angle_2)
    turtle_eyes_2.forward(ghost_size/5)
    turtle_eyes_2.down()
    turtle_eyes_2.setheading(0)
    turtle_eyes_2.up()
    turtle_eyes_2.left(90)
    turtle_eyes_2.left(55)
    turtle_eyes_2.forward(ghost_size/4)
    turtle_eyes_2.down()
    turtle_eyes_2.dot(ghost_size/4, "blue")
    turtle_eyes_2.up()
    turtle_eyes_2.left(180)
    turtle_eyes_2.forward(ghost_size/4)
    turtle_eyes_2.left(70)
    turtle_eyes_2.forward(ghost_size/4)
    turtle_eyes_2.dot(ghost_size/4, "blue")

# - Create the ghost turtle 3
turtle_ghost_3 = turtle.Turtle()
turtle_ghost_3.hideturtle()
turtle_ghost_3.up()
turtle_ghost_3.goto(ghost_start_x, ghost_start_y)
turtle_ghost_3.down()
ghost_x_3 = ghost_start_x
ghost_y_3 = ghost_start_y
ghost_3 = {"turtle":turtle_ghost_3, "move":"left"}
ghosts.append(ghost_3)

# - Create ghost face 3
turtle_ghost_face_3 = turtle.Turtle()
turtle_ghost_face_3.hideturtle()
turtle_eyes_3 = turtle.Turtle()
turtle_eyes_3.hideturtle()
def draw_face_of_ghost_3(eyes_angle_3):
    turtle_ghost_face_3.color("pink", "pink")
    turtle_ghost_face_3.setheading(0)
    turtle_ghost_face_3.up()
    turtle_ghost_face_3.dot(ghost_size)
    turtle_ghost_face_3.up()
    turtle_ghost_face_3.left(90)
    turtle_ghost_face_3.left(55)
    turtle_ghost_face_3.forward(ghost_size/4)
    turtle_ghost_face_3.down()
    turtle_ghost_face_3.dot(ghost_size/2.5, "white")
    turtle_ghost_face_3.up()
    turtle_ghost_face_3.left(180)
    turtle_ghost_face_3.forward(ghost_size/4)
    turtle_ghost_face_3.left(70)
    turtle_ghost_face_3.forward(ghost_size/4)
    turtle_ghost_face_3.dot(ghost_size/2.5, "white")
    turtle_eyes_3.setheading(0)
    turtle_eyes_3.up()
    turtle_eyes_3.left(eyes_angle_3)
    turtle_eyes_3.forward(ghost_size/5)
    turtle_eyes_3.down()
    turtle_eyes_3.setheading(0)
    turtle_eyes_3.up()
    turtle_eyes_3.left(90)
    turtle_eyes_3.left(55)
    turtle_eyes_3.forward(ghost_size/4)
    turtle_eyes_3.down()
    turtle_eyes_3.dot(ghost_size/4, "blue")
    turtle_eyes_3.up()
    turtle_eyes_3.left(180)
    turtle_eyes_3.forward(ghost_size/4)
    turtle_eyes_3.left(70)
    turtle_eyes_3.forward(ghost_size/4)
    turtle_eyes_3.dot(ghost_size/4, "blue")
    
# - Create the ghost turtle 4
turtle_ghost_4 = turtle.Turtle()
turtle_ghost_4.hideturtle()
turtle_ghost_4.up()
turtle_ghost_4.goto(ghost_start_x, ghost_start_y)
turtle_ghost_4.down()
ghost_x_4 = ghost_start_x
ghost_y_4 = ghost_start_y
ghost_4 = {"turtle":turtle_ghost_4, "move":"left"}
ghosts.append(ghost_4)

# - Create ghost face 4
turtle_ghost_face_4 = turtle.Turtle()
turtle_ghost_face_4.hideturtle()
turtle_eyes_4 = turtle.Turtle()
turtle_eyes_4.hideturtle()
def draw_face_of_ghost_4(eyes_angle_4):
    turtle_ghost_face_4.color("purple", "purple")
    turtle_ghost_face_4.setheading(0)
    turtle_ghost_face_4.up()
    turtle_ghost_face_4.dot(ghost_size)
    turtle_ghost_face_4.up()
    turtle_ghost_face_4.left(90)
    turtle_ghost_face_4.left(55)
    turtle_ghost_face_4.forward(ghost_size/4)
    turtle_ghost_face_4.down()
    turtle_ghost_face_4.dot(ghost_size/2.5, "white")
    turtle_ghost_face_4.up()
    turtle_ghost_face_4.left(180)
    turtle_ghost_face_4.forward(ghost_size/4)
    turtle_ghost_face_4.left(70)
    turtle_ghost_face_4.forward(ghost_size/4)
    turtle_ghost_face_4.dot(ghost_size/2.5, "white")
    turtle_eyes_4.setheading(0)
    turtle_eyes_4.up()
    turtle_eyes_4.left(eyes_angle_4)
    turtle_eyes_4.forward(ghost_size/5)
    turtle_eyes_4.down()
    turtle_eyes_4.setheading(0)
    turtle_eyes_4.up()
    turtle_eyes_4.left(90)
    turtle_eyes_4.left(55)
    turtle_eyes_4.forward(ghost_size/4)
    turtle_eyes_4.down()
    turtle_eyes_4.dot(ghost_size/4, "blue")
    turtle_eyes_4.up()
    turtle_eyes_4.left(180)
    turtle_eyes_4.forward(ghost_size/4)
    turtle_eyes_4.left(70)
    turtle_eyes_4.forward(ghost_size/4)
    turtle_eyes_4.dot(ghost_size/4, "blue")

# - Handle the movement keys
def move_up():
    global next_move
    next_move = "up"

def move_down():
    global next_move
    next_move = "down"

def move_left():
    global next_move
    next_move = "left"

def move_right():
    global next_move
    next_move = "right"

# - Handle cheat mode
cheat_number = 0
def cheat_mode():
    global cheat_number
    cheat_number += 1
    
# - Set up the key press events
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(cheat_mode, "c")

# - Need to use listen for key events to work
turtle.listen()


# - Determine the movement of pacman
# - Determine if pacman hits a wall or food

# - Game main loop
def game_loop():
    global current_move, next_move
    global pacman_x, pacman_y
    global ghost_x_1, ghost_y_1, ghost_x_2, ghost_y_2, ghost_x_3, ghost_y_3, ghost_x_4, ghost_y_4
    global ghosts, ghost_1, ghost_2, ghost_3, ghost_4
    global food_count, setheading_angle
    global score

    turtle_fan.clear()
    turtle_score.clear()
    turtle_ghost_face_1.clear()
    turtle_eyes_1.clear()
    turtle_ghost_face_2.clear()
    turtle_eyes_2.clear()
    turtle_ghost_face_3.clear()
    turtle_eyes_3.clear()
    turtle_ghost_face_4.clear()
    turtle_eyes_4.clear()

    # - Handle the pacman next move
    # - Update the condition of the following if statement so that
    #   pacman can only move along the rows and columns of the maze
    if (pacman_x - maze_x) % tile_size == 0 and (pacman_y - maze_y) % tile_size == 0 \
       and next_move != "":
        current_move = next_move
        next_move = ""

    # - Find the pacman new position
    if current_move == "up":
        new_x = pacman_x
        new_y = pacman_y + pacman_speed
        setheading_angle = 90
    elif current_move == "down":
        new_x = pacman_x
        new_y = pacman_y - pacman_speed
        setheading_angle = (-90)
    elif current_move == "right":
        new_x = pacman_x + pacman_speed
        new_y = pacman_y
        setheading_angle = (0)
    elif current_move == "left":
        new_x = pacman_x - pacman_speed
        new_y = pacman_y
        setheading_angle = (180)
    else:
        new_x = pacman_x
        new_y = pacman_y

    
        
    # - Handle the collision of pacman, food and walls
    for i in range(maze_columns):
        for j in range(maze_rows):
            # Get the tile
            tile = maze[j][i]

            # - Locate the tile and calculate the distance
            tile_x= maze_x+ i*tile_size
            tile_y= maze_y +(maze_rows- j- 1)*tile_size
            dx0 = math.fabs(tile_x - new_x)
            dy0 = math.fabs(tile_y - new_y)


            # - Collision detection
            # If pacman collides with any wall, stop pacman from moving
            # If pacman collides with any food, eat the food (remove the food)
            if tile == "+" and dx0 < (pacman_size + tile_size) / 2 and dy0 < (pacman_size + tile_size) / 2:
                new_x = pacman_x
                new_y = pacman_y
            elif tile == "." and dx0 < (pacman_size + food_size) / 2 and dy0 < (pacman_size + food_size) / 2:
                maze[j] = maze[j][:i] + "-" + maze[j][i+1:]
                turtle.goto(tile_x, tile_y)
                turtle.color("black", "black")
                turtle.dot(food_size)
                food_count = food_count - 1
                score += 1
            elif tile == "o" and dx0 < (pacman_size + food_size) / 2 and dy0 < (pacman_size + food_size) / 2:
                maze[j] = maze[j][:i] + "*" + maze[j][i+1:]
                turtle.goto(tile_x, tile_y)
                turtle.color("black", "black")
                turtle.dot(food_size)
                food_count = food_count - 1
                score = score + 5
        
    # - Move the pacman
    if new_x < maze_x:
        turtle_pacman.up()
        turtle_fan.up()
        turtle_pacman.goto(maze_x + (maze_columns - 1) * tile_size, new_y)
        turtle_fan.goto(maze_x + (maze_columns - 1) * tile_size, new_y)
        turtle_pacman.down()
        turtle_fan.down()
        pacman_x = (maze_x + (maze_columns - 1) * tile_size)
        pacman_y = new_y
    elif new_x > (maze_x + (maze_columns - 1) * tile_size):
        turtle_pacman.up()
        turtle_fan.up()
        turtle_pacman.goto(maze_x, new_y)
        turtle_fan.goto(maze_x, new_y)
        turtle_pacman.down()
        turtle_fan.down()
        pacman_x = maze_x
        pacman_y = new_y
    elif new_y < maze_y:
        turtle_pacman.up()
        turtle_fan.up()
        turtle_pacman.goto(new_x, maze_y + (maze_rows - 1) * tile_size)
        turtle_fan.goto(new_x, maze_y + (maze_rows - 1) * tile_size)
        turtle_pacman.down()
        turtle_fan.down()
        pacman_x = new_x
        pacman_y = (maze_y + (maze_rows - 1) * tile_size)
    elif new_y > (maze_y + (maze_rows - 1) * tile_size):
        turtle_pacman.up()
        turtle_fan.up()
        turtle_pacman.goto(new_x, maze_y)
        turtle_fan.goto(new_x, maze_y)
        turtle_pacman.down()
        turtle_fan.down()
        pacman_x = new_x
        pacman_y = maze_y
    else:
        turtle_pacman.up()
        turtle_fan.up()
        turtle_pacman.goto(new_x, new_y)
        turtle_fan.goto(new_x, new_y)
        turtle_pacman.down()
        turtle_fan.down()
        pacman_x = new_x
        pacman_y = new_y

    # - Pacman's mouth movment
    if cheat_number % 2 == 0:
        draw_pacman(setheading_angle, "yellow")
    elif cheat_number % 2 == 1:
        draw_pacman(setheading_angle, "green")

    # - Determine the moves for the ghost 1
    moves_1 = []
    for i in range(1):
        i = int((ghost_x_1 - maze_x) / tile_size)
        j = (maze_rows - 1) - int((ghost_y_1 - maze_y) / tile_size)
        if (ghost_x_1 - maze_x) % tile_size == 0 and (ghost_y_1 - maze_y) % tile_size == 0:
            if ghost_x_1 >= (maze_x + (maze_columns - 1) * tile_size):
                moves_1.append("left")
            if ghost_x_1 <= maze_x:
                moves_1.append("right")
            if ghost_y_1 >= (maze_y + (maze_rows - 1) * tile_size):
                moves_1.append("down")
            if ghost_y_1 <= maze_y:
                moves_1.append("up")
            if  maze_x < ghost_x_1 < (maze_x + (maze_columns - 1) * tile_size) and \
               maze_y < ghost_y_1 < (maze_y + (maze_rows - 1) * tile_size):
                if j > 0 and maze[j - 1][i] != "+":
                    moves_1.append("up")
                if j > 0 and maze[j + 1][i] != "+":
                    moves_1.append("down")
                if i > 0 and maze[j][i - 1] != "+":
                    moves_1.append("left")
                if i > 0 and maze[j][i + 1] != "+":
                    moves_1.append("right")
        if len(moves_1) >= 2:
            if ghost_1["move"] == "up":
                if "down" in moves_1:
                    moves_1.remove("down")
            if ghost_1["move"] == "down":
                if "up" in moves_1:
                    moves_1.remove("up")
            if ghost_1["move"] == "left":
                if "right" in moves_1:
                    moves_1.remove("right")
            if ghost_1["move"] == "right":
                if "left" in moves_1:
                    moves_1.remove("left")
            ghost_1["move"] = random.choice(moves_1)
        elif len(moves_1) == 1:
            ghost_1["move"] = moves_1[0]

    # - Find the ghost 1 new position
    if ghost_1["move"] == "up":
        ghost_new_x_1 = ghost_x_1
        ghost_new_y_1 = ghost_y_1 + ghost_speed
        eyes_angle_1 = 90
    elif ghost_1["move"] == "down":
        ghost_new_x_1 = ghost_x_1
        ghost_new_y_1 = ghost_y_1 - ghost_speed
        eyes_angle_1 = -90
    elif ghost_1["move"] == "right":
        ghost_new_x_1 = ghost_x_1 + ghost_speed
        ghost_new_y_1 = ghost_y_1
        eyes_angle_1 = 0
    elif ghost_1["move"] == "left":
        ghost_new_x_1 = ghost_x_1 - ghost_speed
        ghost_new_y_1 = ghost_y_1
        eyes_angle_1 = 180
    else:
        ghost_new_x_1 = ghost_x_1
        ghost_new_y_1 = ghost_y_1

    # - Move the ghost 1
    turtle_ghost_1.up()
    turtle_ghost_face_1.up()
    turtle_eyes_1.up()
    ghost_1["turtle"].goto(ghost_new_x_1, ghost_new_y_1)
    turtle_ghost_face_1.goto(ghost_new_x_1, ghost_new_y_1)
    turtle_eyes_1.goto(ghost_new_x_1, ghost_new_y_1)
    ghost_x_1 = ghost_1["turtle"].xcor()
    ghost_y_1 = ghost_1["turtle"].ycor()
    turtle_ghost_face_1.down()
    turtle_eyes_1.down()
    turtle_ghost_1.down()

    # - Draw face of ghost 1
    draw_face_of_ghost_1(eyes_angle_1)

    # - Determine the moves for the ghost 2
    moves_2 = []
    for i in range(1):
        i = int((ghost_x_2 - maze_x) / tile_size)
        j = (maze_rows - 1) - int((ghost_y_2 - maze_y) / tile_size)
        if (ghost_x_2 - maze_x) % tile_size == 0 and (ghost_y_2 - maze_y) % tile_size == 0:
            if ghost_x_2 >= (maze_x + (maze_columns - 1) * tile_size):
                moves_2.append("left")
            if ghost_x_2 <= maze_x:
                moves_2.append("right")
            if ghost_y_2 >= (maze_y + (maze_rows - 1) * tile_size):
                moves_2.append("down")
            if ghost_y_2 <= maze_y:
                moves_2.append("up")
            if  maze_x < ghost_x_2 < (maze_x + (maze_columns - 1) * tile_size) and \
               maze_y < ghost_y_2 < (maze_y + (maze_rows - 1) * tile_size):
                if j > 0 and maze[j - 1][i] != "+":
                    moves_2.append("up")
                if j > 0 and maze[j + 1][i] != "+":
                    moves_2.append("down")
                if i > 0 and maze[j][i - 1] != "+":
                    moves_2.append("left")
                if i > 0 and maze[j][i + 1] != "+":
                    moves_2.append("right")
        if len(moves_2) >= 2:
            if ghost_2["move"] == "up":
                if "down" in moves_2:
                    moves_2.remove("down")
            if ghost_2["move"] == "down":
                if "up" in moves_2:
                    moves_2.remove("up")
            if ghost_2["move"] == "left":
                if "right" in moves_2:
                    moves_2.remove("right")
            if ghost_2["move"] == "right":
                if "left" in moves_2:
                    moves_2.remove("left")
            ghost_2["move"] = random.choice(moves_2)
        elif len(moves_2) == 1:
            ghost_2["move"] = moves_2[0]

    # - Find the ghost 2 new position
    if ghost_2["move"] == "up":
        ghost_new_x_2 = ghost_x_2
        ghost_new_y_2 = ghost_y_2 + ghost_speed
        eyes_angle_2 = 90
    elif ghost_2["move"] == "down":
        ghost_new_x_2 = ghost_x_2
        ghost_new_y_2 = ghost_y_2 - ghost_speed
        eyes_angle_2 = -90
    elif ghost_2["move"] == "right":
        ghost_new_x_2 = ghost_x_2 + ghost_speed
        ghost_new_y_2 = ghost_y_2
        eyes_angle_2 = 0
    elif ghost_2["move"] == "left":
        ghost_new_x_2 = ghost_x_2 - ghost_speed
        ghost_new_y_2 = ghost_y_2
        eyes_angle_2 = 180
    else:
        ghost_new_x_2 = ghost_x_2
        ghost_new_y_2 = ghost_y_2

    # - Move the ghost 2
    turtle_ghost_2.up()
    turtle_ghost_face_2.up()
    turtle_eyes_2.up()
    ghost_2["turtle"].goto(ghost_new_x_2, ghost_new_y_2)
    turtle_ghost_face_2.goto(ghost_new_x_2, ghost_new_y_2)
    turtle_eyes_2.goto(ghost_new_x_2, ghost_new_y_2)
    ghost_x_2 = ghost_2["turtle"].xcor()
    ghost_y_2 = ghost_2["turtle"].ycor()
    turtle_ghost_face_2.down()
    turtle_eyes_2.down()
    turtle_ghost_2.down()

    # - Draw face of ghost 2
    draw_face_of_ghost_2(eyes_angle_2)

    # - Determine the moves for the ghost 3
    moves_3 = []
    for i in range(1):
        i = int((ghost_x_3 - maze_x) / tile_size)
        j = (maze_rows - 1) - int((ghost_y_3 - maze_y) / tile_size)
        if (ghost_x_3 - maze_x) % tile_size == 0 and (ghost_y_3 - maze_y) % tile_size == 0:
            if ghost_x_3 >= (maze_x + (maze_columns - 1) * tile_size):
                moves_3.append("left")
            if ghost_x_3 <= maze_x:
                moves_3.append("right")
            if ghost_y_3 >= (maze_y + (maze_rows - 1) * tile_size):
                moves_3.append("down")
            if ghost_y_3 <= maze_y:
                moves_3.append("up")
            if  maze_x < ghost_x_3 < (maze_x + (maze_columns - 1) * tile_size) and \
               maze_y < ghost_y_3 < (maze_y + (maze_rows - 1) * tile_size):
                if j > 0 and maze[j - 1][i] != "+":
                    moves_3.append("up")
                if j > 0 and maze[j + 1][i] != "+":
                    moves_3.append("down")
                if i > 0 and maze[j][i - 1] != "+":
                    moves_3.append("left")
                if i > 0 and maze[j][i + 1] != "+":
                    moves_3.append("right")
        if len(moves_3) >= 2:
            if ghost_3["move"] == "up":
                if "down" in moves_3:
                    moves_3.remove("down")
            if ghost_3["move"] == "down":
                if "up" in moves_3:
                    moves_3.remove("up")
            if ghost_3["move"] == "left":
                if "right" in moves_3:
                    moves_3.remove("right")
            if ghost_3["move"] == "right":
                if "left" in moves_3:
                    moves_3.remove("left")
            ghost_3["move"] = random.choice(moves_3)
        elif len(moves_3) == 1:
            ghost_3["move"] = moves_3[0]

    # - Find the ghost 3 new position
    if ghost_3["move"] == "up":
        ghost_new_x_3 = ghost_x_3
        ghost_new_y_3 = ghost_y_3 + ghost_speed
        eyes_angle_3 = 90
    elif ghost_3["move"] == "down":
        ghost_new_x_3 = ghost_x_3
        ghost_new_y_3 = ghost_y_3 - ghost_speed
        eyes_angle_3 = -90
    elif ghost_3["move"] == "right":
        ghost_new_x_3 = ghost_x_3 + ghost_speed
        ghost_new_y_3 = ghost_y_3
        eyes_angle_3 = 0
    elif ghost_3["move"] == "left":
        ghost_new_x_3 = ghost_x_3 - ghost_speed
        ghost_new_y_3 = ghost_y_3
        eyes_angle_3 = 180
    else:
        ghost_new_x_3 = ghost_x_3
        ghost_new_y_3 = ghost_y_3

    # - Move the ghost 3
    turtle_ghost_3.up()
    turtle_ghost_face_3.up()
    turtle_eyes_3.up()
    ghost_3["turtle"].goto(ghost_new_x_3, ghost_new_y_3)
    turtle_ghost_face_3.goto(ghost_new_x_3, ghost_new_y_3)
    turtle_eyes_3.goto(ghost_new_x_3, ghost_new_y_3)
    ghost_x_3 = ghost_3["turtle"].xcor()
    ghost_y_3 = ghost_3["turtle"].ycor()
    turtle_ghost_face_3.down()
    turtle_eyes_3.down()
    turtle_ghost_3.down()

    # - Draw face of ghost 3
    draw_face_of_ghost_3(eyes_angle_3)

    # - Determine the moves for the ghost 4
    moves_4 = []
    for i in range(1):
        i = int((ghost_x_4 - maze_x) / tile_size)
        j = (maze_rows - 1) - int((ghost_y_4 - maze_y) / tile_size)
        if (ghost_x_4 - maze_x) % tile_size == 0 and (ghost_y_4 - maze_y) % tile_size == 0:
            if ghost_x_4 >= (maze_x + (maze_columns - 1) * tile_size):
                moves_4.append("left")
            if ghost_x_4 <= maze_x:
                moves_4.append("right")
            if ghost_y_4 >= (maze_y + (maze_rows - 1) * tile_size):
                moves_4.append("down")
            if ghost_y_4 <= maze_y:
                moves_4.append("up")
            if  maze_x < ghost_x_4 < (maze_x + (maze_columns - 1) * tile_size) and \
               maze_y < ghost_y_4 < (maze_y + (maze_rows - 1) * tile_size):
                if j > 0 and maze[j - 1][i] != "+":
                    moves_4.append("up")
                if j > 0 and maze[j + 1][i] != "+":
                    moves_4.append("down")
                if i > 0 and maze[j][i - 1] != "+":
                    moves_4.append("left")
                if i > 0 and maze[j][i + 1] != "+":
                    moves_4.append("right")
        if len(moves_4) >= 2:
            if ghost_4["move"] == "up":
                if "down" in moves_4:
                    moves_4.remove("down")
            if ghost_4["move"] == "down":
                if "up" in moves_4:
                    moves_4.remove("up")
            if ghost_4["move"] == "left":
                if "right" in moves_4:
                    moves_4.remove("right")
            if ghost_4["move"] == "right":
                if "left" in moves_4:
                    moves_4.remove("left")
            ghost_4["move"] = random.choice(moves_4)
        elif len(moves_4) == 1:
            ghost_4["move"] = moves_4[0]

    # - Find the ghost 4 new position
    if ghost_4["move"] == "up":
        ghost_new_x_4 = ghost_x_4
        ghost_new_y_4 = ghost_y_4 + ghost_speed
        eyes_angle_4 = 90
    elif ghost_4["move"] == "down":
        ghost_new_x_4 = ghost_x_4
        ghost_new_y_4 = ghost_y_4 - ghost_speed
        eyes_angle_4 = -90
    elif ghost_4["move"] == "right":
        ghost_new_x_4 = ghost_x_4 + ghost_speed
        ghost_new_y_4 = ghost_y_4
        eyes_angle_4 = 0
    elif ghost_4["move"] == "left":
        ghost_new_x_4 = ghost_x_4 - ghost_speed
        ghost_new_y_4 = ghost_y_4
        eyes_angle_4 = 180
    else:
        ghost_new_x_4 = ghost_x_4
        ghost_new_y_4 = ghost_y_4

    # - Move the ghost 4
    turtle_ghost_4.up()
    turtle_ghost_face_4.up()
    turtle_eyes_4.up()
    ghost_4["turtle"].goto(ghost_new_x_4, ghost_new_y_4)
    turtle_ghost_face_4.goto(ghost_new_x_4, ghost_new_y_4)
    turtle_eyes_4.goto(ghost_new_x_4, ghost_new_y_4)
    ghost_x_4 = ghost_4["turtle"].xcor()
    ghost_y_4 = ghost_4["turtle"].ycor()
    turtle_ghost_face_4.down()
    turtle_eyes_4.down()
    turtle_ghost_4.down()

    # - Draw face of ghost 4
    draw_face_of_ghost_4(eyes_angle_4)
    
    # - Count Score
    turtle_score.write("Score:" + str(score), font = ("Times", 20, "bold"), align = "center")

    # Update the window content
    turtle.update()
     
    if cheat_number % 2 == 0:
        
        # - Handle ghost 1 Game Over situations
        for i in range(1):
            ghost_x_1 = ghost_1["turtle"].xcor()
            ghost_y_1 = ghost_1["turtle"].ycor()
            
            dx1 = math.fabs(ghost_x_1 - pacman_x)
            dy1 = math.fabs(ghost_y_1- pacman_y)
            #print(ghost_x, pacman_x, dx2, ghost_y, pacman_y, dy2)
    
            if dx1 < (ghost_size + pacman_size) / 2 and dy1 < (ghost_size + pacman_size) / 2:
                turtle.color("red")
                turtle.up()
                turtle.home()
                turtle.down()
                turtle.write("Game over!", font = ("Times", 50, "bold"), align = "center")
                return
            
        # - Handle ghost 2 Game Over situations
        for i in range(1):
            ghost_x_2 = ghost_2["turtle"].xcor()
            ghost_y_2 = ghost_2["turtle"].ycor()
            
            dx2 = math.fabs(ghost_x_2 - pacman_x)
            dy2 = math.fabs(ghost_y_2 - pacman_y)
            #print(ghost_x, pacman_x, dx2, ghost_y, pacman_y, dy2)
    
            if dx2 < (ghost_size + pacman_size) / 2 and dy2 < (ghost_size + pacman_size) / 2:
                turtle.color("red")
                turtle.up()
                turtle.home()
                turtle.down()
                turtle.write("Game over!", font = ("Times", 50, "bold"), align = "center")
                return
    
        # - Handle ghost 3 Game Over situations
        for i in range(1):
            ghost_x_3 = ghost_3["turtle"].xcor()
            ghost_y_3 = ghost_3["turtle"].ycor()
            
            dx3 = math.fabs(ghost_x_3 - pacman_x)
            dy3 = math.fabs(ghost_y_3 - pacman_y)
            #print(ghost_x, pacman_x, dx2, ghost_y, pacman_y, dy2)
    
            if dx3 < (ghost_size + pacman_size) / 2 and dy3 < (ghost_size + pacman_size) / 2:
                turtle.color("red")
                turtle.up()
                turtle.home()
                turtle.down()
                turtle.write("Game over!", font = ("Times", 50, "bold"), align = "center")
                return

        # - Handle ghost 4 Game Over situations
        for i in range(1):
            ghost_x_4 = ghost_4["turtle"].xcor()
            ghost_y_4 = ghost_4["turtle"].ycor()
            
            dx4 = math.fabs(ghost_x_4 - pacman_x)
            dy4 = math.fabs(ghost_y_4 - pacman_y)
            #print(ghost_x, pacman_x, dx2, ghost_y, pacman_y, dy2)
    
            if dx4 < (ghost_size + pacman_size) / 2 and dy4 < (ghost_size + pacman_size) / 2:
                turtle.color("red")
                turtle.up()
                turtle.home()
                turtle.down()
                turtle.write("Game over!", font = ("Times", 50, "bold"), align = "center")
                return
        
    # - Handle Win situations
    if food_count == 0:
        turtle.color("white")
        turtle.up()
        turtle.home()
        turtle.down()
        turtle.write("You win!", font = ("Times", 50, "bold"), align = "center")
        return
        
    # Keep on running the game loop
    turtle.ontimer(game_loop, frame_time)


# Start the game loop
game_loop()

turtle.done()
