import random
import time
import turtle


spawn_interval = 1
ball_speed = 0.1
increase_rotation_step = 1
colour_change_interval = 1

# Set up window
window =  turtle.Screen()
window.bgcolor(0.2, 0.2, 0.2)
window.tracer(0)

spinner = turtle.Turtle()
spinner.color("white")
spinner.rotation_speed = 0.5

# Spawn new balls
colour = random.random(), random.random(), random.random()

balls = []
pool_of_balls = []

def spawn_ball(reference):
    if pool_of_balls:
        balls.append(pool_of_balls.pop())
        balls[-1].showturtle()
    else:
        balls.append(turtle.Turtle())
    balls[-1].shape("triangle")
    balls[-1].color(colour)
    balls[-1].turtlesize(0.5)
    balls[-1].penup()
    balls[-1].setposition(reference.position())
    balls[-1].setheading(reference.heading())

# Change speed of rotation
def increase_anticlockwise_rotation():
    spinner.rotation_speed += increase_rotation_step

def decrease_anticlockwise_rotation():
    spinner.rotation_speed -= increase_rotation_step

window.onkeypress(increase_anticlockwise_rotation, "Left")
window.onkeypress(decrease_anticlockwise_rotation, "Right")
window.listen()

# Main animation loop
spawn_timer = time.time()
ball_colour_timer = time.time()
while True:
    spinner.left(spinner.rotation_speed)

    # Spawn new ball
    if time.time() - spawn_timer > spawn_interval:
        spawn_ball(spinner)
        spawn_timer = time.time()

    # Change ball colour
    if time.time() - ball_colour_timer > colour_change_interval:
        colour = random.random(), random.random(), random.random()
        #ball_colour_timer = time.time()
        ball_colour_timer =+ 6

    # Move all balls and clear balls that leave the screen
    for ball in balls.copy():
        ball.forward(ball_speed)
        # Check if ball has left the screen
        if (
            abs(ball.xcor()) > window.window_width() / 2
            or abs(ball.ycor()) > window.window_height() / 2
        ):
            ball.hideturtle()
            balls.remove(ball)
            pool_of_balls.append(ball)

    #print(len(balls), len(pool_of_balls), len(turtle.turtles()))
    window.update()