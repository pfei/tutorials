

# https://www.frederic-junier.org/PythonSeconde/Python_Seconde_Parc/tortue/tortue1.html
# https://www.frederic-junier.org/PythonSeconde/Python_Seconde_Parc/tortue/tortue2.html
# (code modifié)


import turtle
import time
import math

bob = turtle.Turtle()
bob.speed(3)      # parametrage de la vitesse 
# : de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide

# gestion des déplacements

# Un carré obtenu par déplacements absolus
bob.up()       #lever le crayon
bob.goto(0,0)
bob.down()     #poser le crayon
bob.goto(100, 0)
bob.goto(100, 100)
bob.goto(0,100)
bob.goto(0,0)

# on attend 3 secondes et on ré-initialise la tortue bob
time.sleep(3)
bob.reset()




# Le même carré obtenu par déplacements relatifs :
for i in range(4):
  print(i)
  bob.forward(100)
  bob.left(90)

# on attend 3 secondes et on ré-initialise la tortue bob
time.sleep(3)
bob.reset()

# Exécuter le code ci-dessous pour tester quelques fonctions basiques de turtle.

bob.speed(5)            #parametrage de la vitesse de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide
bob.shape("turtle")     #choix de la forme de la tortue
bob.pencolor("red")     #choix de la couleur du crayon
bob.pensize(4)          #épaisseur du crayon
bob.up()                #lever le crayon     
bob.goto(0,0)           # aller à la position (0,0)
bob.setheading(0)       #orientation de la tortue vers l'Est / 90  Nord / 180 Ouest / 270 Sud
bob.down()              #poser le crayon
for k in range(4):
  bob.forward(100)    # avancer de 100 pixels
  bob.left(90)        # tourner de 90 degrés

turtle.done()
