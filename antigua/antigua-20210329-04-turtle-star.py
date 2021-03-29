

# adapted from:
# https://docs.python.org/3/library/turtle.html

import turtle

t = turtle.Turtle()

t.color('red', 'yellow')
t.begin_fill()

for i in range(36):
    t.forward(200)
    t.left(170)

t.end_fill()

turtle.done()