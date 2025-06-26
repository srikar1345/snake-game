from turtle import Turtle,Screen
#from turtle import * this method imports everything,not usuallly used in the python comunity for less cofusion in code
#from turlte as t giving and alias to the module name for future reference
tim=Turtle()
tim.shape("turtle")
tim.color("red")
tim.forward(100)#the distance is specified in the brackets
tim.right(90)#in the brackets the angle is specified by how much the turtle shoulbe rotated in right direction
tim.forward(10)
tim.right(90)
#for the dashed line
tim.penup()
tim.forward(10)
tim.pendown()



















screen=Screen()
screen.exitonclick()