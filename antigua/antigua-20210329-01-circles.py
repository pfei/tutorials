
# https://docs.python.org/3/library/turtle.html

# adapted from :
# https://docs.python.org/3/library/turtle.html#turtle.circle

import turtle

t = turtle.Turtle()
t.pensize(3)

# go to starting point:
t.home()
print(t.position())
    # should print: (0.00,0.00)
print(t.heading())
    # should print: 0.0

# draw a circle: 
t.color('purple')
t.circle(50)
print(t.position())
    # should print: (0.00,0.00)
print(t.heading())
    # should print: 0.0

# draw a semicircle: 
t.color('blue')
t.circle(120, 180)

print(t.position())
    # should print: (0.00,240)
print(t.heading())
    # should print: 180.0

turtle.done()
