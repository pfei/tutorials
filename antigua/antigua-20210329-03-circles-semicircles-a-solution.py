


# goal: draw this:
# https://github.com/pfei/tutorials/blob/main/images/antigua-20210329-03-circles-semicircles-a-solution.png

# https://docs.python.org/3/library/turtle.html#turtle.circle

import turtle

t = turtle.Turtle()
t.pensize(2)


####################
# TRY TO DO IT 
# BEFORE READING 
# A SOLUTION BELOW

# you may run it
# without looking at the code itself
####################


















# go to starting point (not necessary here, but more explicit):
t.home()
# print(t.position())
# print(t.heading())


t.color('purple')
t.circle(30)

t.color('red')
t.circle(40, 180)

t.color('purple')
t.circle(50)

t.color('red')
t.circle(60, 180)

t.color('purple')
t.circle(70)


turtle.done()
