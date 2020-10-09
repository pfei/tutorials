import turtle

t = turtle.Turtle()
t.pensize(3)

for c in ['red', 'green', 'yellow', 'blue']:
    print(c)
    t.color(c)
    t.forward(100)
    t.left(90)

turtle.done()