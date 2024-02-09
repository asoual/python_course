from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()


def move_forward():
    my_turtle.forward(10)
def move_backward():
    my_turtle.backward(10)
def turn_left():
    my_turtle.left(10)
def turn_right():
    my_turtle.right(10)
def clear():
    my_turtle.penup()
    my_turtle.home()
    my_turtle.clear()
    my_turtle.pendown()
    
screen.onkey(key="z",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="q",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)
screen.listen()

screen.exitonclick()