from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="who will win this race? Enter a color: ")
colors = ["red", "green", "blue", "orange","brown","black","pink"]
y_positions = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []
finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(x = 280, y =190)
finish_line.right(90)
finish_line.pendown()
finish_line.width(5)
finish_line.forward(380)
for i in range(0, len(colors)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x= -270,y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > finish_line.xcor()-20:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
screen.exitonclick()