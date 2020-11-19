

# calcul de la longueur de l'hypoténuse

import math

def hypotenuse(c1, c2):
    return math.sqrt(c1*c1 + c2*c2)

# h = hypotenuse(3, 4)
# print(h)

c1 = int(input("longueur premier coté : "))
c2 = int(input("longueur deuxième coté : "))
h = hypotenuse(c1, c2)
print('hypoténuse : ', h)
