
import turtle

alice = turtle.Turtle()

alice.up()
alice.dot(5)
alice.goto(-100,-100)
alice.dot(20, "blue")
alice.goto(-100,100)
alice.dot(20, "red")
alice.goto(100,100)
alice.dot(20, "yellow")
alice.goto(100,-100)
alice.dot(20, "green")

turtle.done()