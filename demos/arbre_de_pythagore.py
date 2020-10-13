
# https://www.mathweb.fr/euclide/2019/03/19/python-turtle-et-un-arbre-de-pythagore/
# (modifié)


import turtle
import math
from random import uniform

from PIL import Image

################################################################################
def save_image(image_name):
    turtle_screen = turtle.getscreen()
    file_eps = image_name + ".eps"
    turtle_screen.getcanvas().postscript(file=file_eps)
    in_file = Image.open(file_eps)
    file_jpg = file_eps.split('.')[0] + '.jpg'
    in_file.save(file_jpg)
################################################################################


bob = turtle.Turtle()
bob.speed(3)

def change_color():
    e1 = uniform(0,1)
    e2 = uniform(0,1)
    e3 = uniform(0,1)
    return e1,e2,e3

def tree(s,e1,e2,e3):
    if s < 5:
        return
    square(s,e1,e2,e3)
    e1,e2,e3 = change_color()
    bob.forward(s)
    s1 = s / math.sqrt(2)
    bob.left(45)
    tree(s1,e1,e2,e3)
    bob.right(90)
    bob.forward(s1)
    tree(s1,e1,e2,e3)
    bob.back(s1)
    bob.left(45)
    bob.back(s)

def square(s,e1,e2,e3):
    bob.pencolor("white")
    bob.fillcolor(e1,e2,e3)
    bob.begin_fill()
    for i in range(4):
        bob.forward(s)
        bob.right(90)
    bob.end_fill()

e1,e2,e3 = change_color()
bob.penup()
bob.left(180)
bob.forward(100)
bob.right(90)
bob.pendown()
tree(100,e1,e2,e3)

save_image('arbre_de_pythagore')

turtle.exitonclick()
