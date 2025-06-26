from turtle import Turtle,Screen
tim=Turtle()
def draw_shape(num_sides):
    agnle= 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(agnle)
for shape_side_n in range(3,10):
    draw_shape(shape_side_n)
    tim.color("SeaGreen")

screen=Screen()
screen.exitonclick()    