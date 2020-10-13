

# exercice : 
# https://www.frederic-junier.org/PythonSeconde/Python_Seconde_Parc/tortue/tortue2.html
# (code modifié)

import turtle
import time


################################################################################
# mise en place de la tortue
bob = turtle.Turtle()
bob.speed(5)            #parametrage de la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
bob.shape("turtle")     #choix de la forme de la tortue
bob.pencolor("red")     #choix de la couleur du crayon
bob.pensize(4)          #épaisseur du crayon
bob.up()                #lever le crayon     
bob.goto(0,0)           # aller à la position (0,0)
bob.setheading(0)       #orientation de la tortue vers l'Est / 90  Nord / 180 Ouest / 270 Sud
bob.down()              #poser le crayon
################################################################################



################################################################################
# une marche
bob.left(90)
bob.forward(50)
bob.right(90)
bob.forward(50)

time.sleep(5)
bob.clear()
bob.up()
bob.goto(0, 0)
bob.down()
################################################################################



################################################################################
def marche(h):
    bob.left(90)
    bob.forward(h)
    bob.right(90)
    bob.forward(h)

def escalier(n, h):
    for k in range(n):
        marche(h)

escalier(5, 50)

################################################################################


turtle.exitonclick()
