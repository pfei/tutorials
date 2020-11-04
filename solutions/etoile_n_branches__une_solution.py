

# https://codewithsara.com/python-with-sara/python-101/u2-python-turtle-graphics/u2s3-turtle-stars/


import turtle 

star = turtle.Turtle()

n = 7
cote = 150

if n%2 == 1: # c'est-à-dire si n est impair
    # on trace une étoile à n branches
    angle = 180 - 180/n
    for i in range(n):
        star.forward(cote)
        star.right(angle)
else: # cad si n est pair
    # trace une étoile à 2xn branches
    angle = 180 - 180/n
    for i in range(2*n):
        star.forward(cote)
        star.right(angle)
    
turtle.done()


# https://codewithsara.com/python-with-sara/python-101/u2-python-turtle-graphics/u2s3-turtle-stars/
