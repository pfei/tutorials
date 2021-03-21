
# growing star
# source : https://michael0x2a.com/blog/turtle-examples

import turtle 

star = turtle.Turtle()

for i in range(20):
    length = i * 10
    print(length)
    star.forward(i * 10)
    star.right(144)
    
turtle.done()