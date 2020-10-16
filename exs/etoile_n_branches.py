
# tracer une étoile à n branches si n est impair
# ou une étoile à 2n branches si n est pair

import turtle 

star = turtle.Turtle()

n = 12
cote = 150

if n%2 == 1: # c'est-à-dire si n est impair
    # on trace une étoile à n branches
    angle = 0 # à modifier
    for i in range(n):
        pass # à modifier
else: # cad si n est pair
    # on trace une étoile à 2n branches
    angle = 0 # à modifier
    for i in range(n):
        pass # à modifier
    
turtle.done()


