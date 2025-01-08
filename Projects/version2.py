import turtle

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("pink")
t.pendown()

for i in range(1000):
    t.forward(100)
    t.left(58)
    t.right(2)

turtle.exitonclick()
