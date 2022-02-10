from turtle import *
shape ("turtle")
#rychlost
speed(3)
#velikost vysněného domečku
velikost = 100

left(90)
forward(velikost)

right(90)
forward(velikost/2)
left(135)
forward(velikost*3/2)
left(90)
forward(velikost*3/2)
left(135)
forward(velikost/2)

right(90)
forward(velikost)
left(90)

forward(velikost*3/4)
left(90)
forward(velikost/3)
right(90)
forward(velikost/5)
right(90)
forward(velikost/3)
left(90)
forward(velikost*1/4)

exitonclick()
