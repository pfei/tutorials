import turtle

colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

study = turtle.Turtle()

for x in range(360):
    study.pencolor(colors[x % 6])
    study.width(x / 100 + 1)
    study.forward(x)
    study.left(59)

turtle.done()