
# réaliser cette figure
# https://github.com/pfei/tutorials/blob/main/images/turtle_seurat.jpg

# https://michael0x2a.com/blog/turtle-examples
# (modifié)

import turtle 
import time

seurat = turtle.Turtle()

dot_distance = 25
width = 5
height = 3

seurat.penup()


for j in range(height):
    for i in range(width): 
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.goto(0,25*j+25)
     
turtle.done()
