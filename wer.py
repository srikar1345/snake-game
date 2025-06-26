from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

# Set up the screen
screen = Screen()  
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=  Snake()
food=Food()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")
gameis_on=True

while gameis_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
       
        snake.extend()
    
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280 :
        gameis_on=False
    for seg in snake.segments:
        if seg==snake.head:
          pass
        elif snake.head.distance(seg)<10:
            gameis_on=False


screen.exitonclick()




 



