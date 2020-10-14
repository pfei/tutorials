

# https://michael0x2a.com/blog/turtle-examples
# (modifié)

import turtle


################################################################################
silly = turtle.Turtle()
silly.pensize(2)

silly.forward(50)
silly.right(90)     # Rotate clockwise by 90 degrees

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

silly.forward(50)
silly.right(90)

################################################################################


################################################################################
smart = turtle.Turtle()
smart.pencolor('green')
smart.pensize(2)
smart.up()
smart.goto(0, 100)
smart.down()

# Loop 4 times. Everything I want to repeat is 
# *indented* by four spaces.
for i in range(4):
    smart.forward(50)
    smart.right(90)
################################################################################
    
turtle.done()

