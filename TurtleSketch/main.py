from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun= forward, key="w")
screen.onkey(fun= backward, key="s")
screen.onkey(fun= turn_left, key="a")
screen.onkey(fun= turn_right, key="d")
screen.onkey(fun= clear, key="c")
screen.exitonclick()