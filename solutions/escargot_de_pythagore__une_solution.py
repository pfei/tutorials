

# http://www.mathkang.org/cite/expo20003.html

# ici l'escargot part d'abord vers le bas

import turtle
import math

t = turtle.Turtle()
t.shape('triangle')
t.pencolor('blue')
t.pensize(2)
t.up()     
t.goto(0,0)
t.setheading(0)       #orientation de la tortue vers l'Est / 90  Nord / 180 Ouest / 270 Sud
t.down()              #poser le crayon


# solution simple, sans boucle, avec seulement quelques côtés
cote = 100      # longueur des cotés, en pixels
t.left(180)     # demi-tour
t.forward(cote)
