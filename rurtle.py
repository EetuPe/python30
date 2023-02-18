from turtle import Turtle, Screen

turo = Turtle()
turo.shape("turtle")
turo.color("green")
turo.speed("slowest")

for _ in range(0,10):
    turo.forward(200)
    turo.penup()
    turo.backward(300)
    turo.pendown()
    turo.left(90)
    turo.forward(100)
    turo.right(270)

my_screen = Screen()

my_screen.exitonclick()