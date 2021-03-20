

import turtle

alice = turtle.Turtle()
alice.pensize(3)

for c in ['red', 'green', 'yellow', 'blue', 'magenta']:
    print(c)
    alice.color(c)
    alice.forward(75)
    alice.left(72)

