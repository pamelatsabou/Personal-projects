# Star

from turtle import Turtle, Screen

pen = Turtle()
for _ in range(5):
    pen.left(72)
    pen.forward(150)
    pen.right(144)
    pen.forward(150)


my_screen = Screen()
my_screen.exitonclick()