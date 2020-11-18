

import turtle
import time
import random


################################################################################
# outils: afficher, effacer messages
tortue_affichage = turtle.Turtle()
tortue_affichage.hideturtle()

def afficher(tortue, message, abscisse, ordonnee):
    tortue.up()
    tortue.goto(abscisse, ordonnee)
    tortue.down()
    tortue.write(message, font=("Arial", 14, "normal"))

def effacer(tortue):
    tortue.undo()
################################################################################

afficher(tortue_affichage, "couleurs au hasard", 0, 120)



alice = turtle.Turtle()
alice.up()
alice.dot(5)

distance = 0
delta_distance = 20
nb_cercles = 4
nb_points_par_cercle = 8

colors = ['yellow', 'gold', 'orange', 
    'red', 'maroon', 'violet', 'magenta', 'purple', 
    'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 
    'lightgreen', 'green', 'darkgreen', 
    'chocolate', 'brown', 'black', 'gray']

colors = colors[:nb_points_par_cercle]

angle = 360 / nb_points_par_cercle
for i in range(nb_cercles):
    distance = distance + delta_distance
    alice.forward(distance)
    for j in range(nb_points_par_cercle):
        c = colors[ random.randrange(0, nb_points_par_cercle)]
        alice.dot(10, c)
        alice.backward(distance)
        alice.left(angle)
        alice.forward(distance)
    alice.backward(distance)


turtle.done()