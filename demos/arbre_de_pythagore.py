# https://www.mathweb.fr/euclide/2019/03/19/python-turtle-et-un-arbre-de-pythagore/

from turtle import *
import math
from random import uniform

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
    forward(s)
    s1 = s / math.sqrt(2)
    left(45)
    tree(s1,e1,e2,e3)
    right(90)
    forward(s1)
    tree(s1,e1,e2,e3)
    back(s1)
    left(45)
    back(s)

def square(s,e1,e2,e3):
    pencolor("white")
    fillcolor(e1,e2,e3)
    begin_fill()
    for i in range(4):
        forward(s)
        right(90)
    end_fill()

e1,e2,e3 = change_color()
penup()
left(180)
forward(100)
right(90)
pendown()
tree(100,e1,e2,e3)