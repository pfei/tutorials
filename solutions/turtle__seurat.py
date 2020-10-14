
# https://michael0x2a.com/blog/turtle-examples
# (modifié)

import turtle 
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

seurat = turtle.Turtle()

dot_distance = 25
width = 4
height = 3

seurat.penup()

for y in range(height):
    for i in range(width):
        seurat.dot()
        seurat.forward(dot_distance)
    seurat.backward(dot_distance * width)
    seurat.right(90)
    seurat.forward(dot_distance)
    seurat.left(90)

save_image('turtle_seurat')
    
turtle.done()