

import turtle
import time


bob = turtle.Turtle()
bob.up()
bob.dot(5)

distance = 0
delta_distance = 20
nb_cercles = 4
nb_points_par_cercle = 8

angle = 360 / nb_points_par_cercle
for i in range(nb_cercles):
    distance = distance + delta_distance
    bob.forward(distance)
    for j in range(nb_points_par_cercle):
        bob.dot(10, "blue")
        bob.backward(distance)
        bob.left(angle)
        bob.forward(distance)
    bob.backward(distance)


turtle.done()