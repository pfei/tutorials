
import turtle

alice = turtle.Turtle()
alice.color('red')
alice.up()
alice.goto(0,100)
alice.down()

bob = turtle.Turtle()
bob.color('blue')

alice.forward(70)
bob.forward(70)
alice.left(90)
bob.left(90)
alice.forward(70)
bob.forward(70)
alice.left(90)
bob.left(90)
alice.forward(70)
bob.forward(70)
alice.left(90)
bob.left(90)
alice.forward(70)
bob.forward(70)
alice.left(90)
bob.left(90)

turtle.done()