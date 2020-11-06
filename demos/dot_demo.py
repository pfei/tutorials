
import turtle
import time


bob = turtle.Turtle()

################################################################################
# https://docs.python.org/3.8/library/turtle.html#turtle.dot
# (adapté)
bob.home()
bob.dot()
bob.fd(50); bob.dot(20, "blue"); bob.fd(50)
print(bob.position())
print(bob.heading())
################################################################################

time.sleep(3)
bob.reset()

################################################################################
bob.up()
bob.dot(10, "blue")
bob.forward(50)
bob.dot(20, "red")
bob.forward(50)
bob.dot(30, "yellow")
bob.forward(50)
bob.dot(40, "green")
################################################################################

time.sleep(3)
bob.reset()

################################################################################
bob.up()
bob.dot(5)
bob.goto(-100,-100)
bob.dot(20, "blue")
bob.goto(-100,100)
bob.dot(20, "red")
bob.goto(100,100)
bob.dot(20, "yellow")
bob.goto(100,-100)
bob.dot(20, "green")
################################################################################

turtle.done()