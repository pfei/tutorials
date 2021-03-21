
# growing star, in random colors
# source : https://michael0x2a.com/blog/turtle-examples
# (source has been modified)

import turtle 
import random


colors = ['yellow', 'gold', 'orange', 
    'red', 'maroon', 'violet', 'magenta', 'purple', 
    'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 
    'lightgreen', 'green', 'darkgreen', 
    'chocolate', 'brown', 'black', 'gray']

nb_of_colors = len(colors)
print('number of colors: ', nb_of_colors)

star = turtle.Turtle()

for i in range(20):
    length = i * 10
    print('side length: ', length)
    c = colors[random.randrange(0, nb_of_colors)]
    print('random color: ', c)
    star.color(c)
    star.forward(i * 10)
    star.right(144)

turtle.done()