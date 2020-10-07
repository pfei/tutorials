
# https://fr.wikibooks.org/wiki/Programmation_Python/Turtle#Tracer_une_spirale_quelconque
# (modifié)

import turtle

alice = turtle.Turtle()


# affichage du titre
alice.up()
alice.goto(0,200)
alice.down()
alice.write("Spirale 1", font=("Arial", 16, "normal"))
alice.up()
alice.goto(0,0)
alice.down()

# affichage de la spirale
alice.speed(10)           
alice.pencolor('purple')
alice.pensize(3)

rayon = 1                  #Le premier rayon par défaut
rayonSpiral = 100
while(rayon < rayonSpiral): 
    alice.circle(rayon, 180)
    rayon += 10             #écartement entre 2 demi-cercle de la spirale

turtle.done()
