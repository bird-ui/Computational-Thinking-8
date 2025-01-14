import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("pink")
t.pendown()

for i in range(100):
    t.forward(11)
    t.left(23)
    t.right(23)
    t.left(67)
    for i in range(14):
        t.forward(15)
        t.left(2)
        t.right(1)
        t.left(6)
        for i in range(5):
            t.forward(1)
            t.left(2)
            t.right(1)
            t.left(6)

turtle.exitonclick()
