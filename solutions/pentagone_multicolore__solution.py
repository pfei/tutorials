
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



alice = turtle.Turtle()
alice.pensize(3)

for c in ['red', 'green', 'yellow', 'blue', 'magenta']:
    print(c)
    alice.color(c)
    alice.forward(75)
    alice.left(72)


# save_image('pentagone_multicolore')

turtle.exitonclick()
