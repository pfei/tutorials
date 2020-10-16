
# https://stackoverflow.com/questions/26455304/python-draw-n-pointed-star-with-turtle-graphics

import sys
import turtle
from time import sleep

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def normal_star(size, color, points):
    if points <= 4:
        raise ValueError('Not enough points')

    turtle.color(color)

    for coprime in range(points // 2, 1, -1):
        if gcd(points, coprime) == 1:

            print("({},{})".format(points, coprime), file=sys.stderr)

            start = turtle.position()

            for _ in range(points):
                turtle.forward(size)
                turtle.left(360.0 / points * coprime)

            turtle.setposition(start)

            return

    abnormal_star(size, color, points)

def abnormal_star(size, color, points):
    # deal with special cases here
    print("Exception:", points, file=sys.stderr)

for points in range(5, 20):
    turtle.reset()
    normal_star(200, 'red', points)
    sleep(5)

turtle.exitonclick()