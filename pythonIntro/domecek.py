from turtle import *
import math
shape ("turtle")
#rychlost
speed(1)
#velikost vysněného domečku
#velikost = 200

def domecek(size):
    diagonal = math.sqrt(2*size**2)

#left(90)
    forward(size)
    left(90)
#right(90)
    forward(size)
    left(45)
    forward(diagonal/2)
    left(90)
    forward(diagonal/2)
    left(135)
    forward(size)
    right(135)
    forward(diagonal)
    right(135)
    forward(size)
    right(135)
    forward(diagonal)
    left(45)

domecek(20)
domecek(20)
domecek(20)
domecek(20)

exitonclick()   