import random
from turtle import Turtle, Screen, colormode

my_turtle = Turtle()
# my_turtle.shape("turtle")
# colors = ["pink", "red", "orange", "darkgoldenrod", "chartreuse3", "cyan3", "blue", "black"]
directions = [0, 90, 180, 270]
my_turtle.speed("fastest")
colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r , g , b)
    return random_color

# draw a square

# for _ in range(4):
#     my_turtle.forward(150)
#     my_turtle.left(90)
# ----------------------------------
# draw a dashed line

# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()
# ----------------------------------
# draw different shapes


# def draw_shape(sides):
#     angle = 360/sides
#     for _ in range(sides):
#         my_turtle.forward(150)
#         my_turtle.left(angle)

# for number_of_sides in range (3,11):
#     my_turtle.color(random.choice(colors))
#     draw_shape(number_of_sides)

# draw a random walk
# my_turtle.pensize(15)
# my_turtle.speed("fast")
# for _ in range(250):
#     my_turtle.color(random_color())
#     my_turtle.forward(40)
#     my_turtle.setheading(random.choice(directions))

#draw a spirograph 
def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        my_turtle.color(random_color())
        my_turtle.circle(75)
        current_heading = my_turtle.heading()
        my_turtle.setheading(current_heading + gap)
draw_spirograph(10)

screen = Screen()
screen.exitonclick()