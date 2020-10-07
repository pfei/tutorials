
import turtle
import time
import math

bob = turtle.Turtle()
bob.speed(3)      # parametrage de la vitesse 
# : de 1 lent à 10 rapide, 0 étant la vitesse la plus rapide

bob.speed(2)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)

longueur_diagonale = math.sqrt(2) * 100

bob.pencolor('red')
bob.left(45)
bob.forward(longueur_diagonale)
print(math.sqrt(2))

bob.left(135)
bob.up()
bob.forward(100)
bob.left(135)
bob.down()
bob.forward(longueur_diagonale)


turtle.done()