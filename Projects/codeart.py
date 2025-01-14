import turtle
t = turtle.Turtle()
colors=["pink","purple","blue"]
#setting speed and start point
t.speed(0)
t.goto(5,5)
t.color("purple")
#main loop for the turtle
for i in range(4):
    t.forward(20)
    t.left(90)

for i in range(20):
    t.color(colors[i%3])
    t.forward(i)
    t.right(5)
    t.left(-5)
    
    t.penup()
    t.goto (100 + i*20,0)
    t.pendown()
    t.right(90)

    for j in range(5):
        t.forward(20)
        t.left(90)
        for k in range(8):
            t.forward(20)
            t.right(45)

    t.penup()
    t.goto (-100 - 20*i,0)
    t.pendown()
    t.right(90)

    for j in range(5):
        t.forward(20)
        t.left(90)
        for k in range(8):
            t.forward(20)
            t.right(45)

    t.penup()
    t.goto (0,-100  - 20*i)
    t.pendown()
    t.right(90)

    for j in range(5):
        t.forward(20)
        t.left(90)
        for k in range(8):
            t.forward(20)
            t.right(45)

    t.penup()
    t.goto (0,100 + 20*i)
    
    t.pendown()
    t.right(90)

    for j in range(5):
        t.forward(20)
        t.left(90)
        for k in range(8):
            t.forward(20)
            t.right(45)
#stop the turtle
turtle.exitonclick()






