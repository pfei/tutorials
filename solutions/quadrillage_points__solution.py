

import turtle 

alice = turtle.Turtle()
alice.penup()

dot_distance = 50

for c in ['red', 'blue']:
    alice.color(c)
    alice.dot()
    alice.forward(dot_distance)

colors = ['red', 'blue']
print(colors[0])
print(colors[1])
print('----------------')

for i in range(5):
    print('i : ' + str(i))
    print('i%2 : ' + str(i%2))
    print(colors[i%2])

