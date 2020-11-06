
import turtle

alice = turtle.Turtle()

alice.up()
alice.goto(-200,0)
distance = 20
taille = 1

for i in range(15):
    alice.dot(taille)
    alice.forward(distance)
    taille = taille + 1

turtle.done()