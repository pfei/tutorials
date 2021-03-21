

# antigua-20210322-03-spiral-in-colors

import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

spiral = turtle.Turtle()

for x in range(50):
    spiral.pencolor(colors[x % 6])
    spiral.width(x / 100 + 1)
    spiral.forward(x)
    spiral.left(59)

turtle.done()
