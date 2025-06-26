from turtle import Turtle,Screen
import random
tim=Turtle()
tim.pensize(15)
directions = [0,90,180,270]
tim.speed("fastest")
for _ in range(200):
 tim.forward(30)
 tim.setheading(random.choice(directions))#the input in the bracket would be the angle in int form


















screen=Screen()
screen.exitonclick()    