# import colorgram
import random
from turtle import Turtle , Screen, colormode
# rgb_colors =[]
# colors = colorgram.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

colormode(255)
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19)
    , (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90)
    , (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

my_turtle = Turtle()
my_turtle.speed("fast")
my_turtle.penup()
my_turtle.hideturtle()
my_turtle.forward(-250)
my_turtle.right(90)
my_turtle.forward(200)
my_turtle.left(90)
my_turtle.pendown()
number_of_dots = 100
for dot_count in range (1 , number_of_dots):
    
    my_turtle.penup()
    my_turtle.dot(20, random.choice(color_list))
    my_turtle.forward(50)
    my_turtle.pendown()
    if dot_count % 10 == 0:
        my_turtle.penup()
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.left(90)
        my_turtle.forward(500)
        my_turtle.left(180)

my_turtle.pendown()
my_turtle.dot(20, random.choice(color_list))




screen = Screen()
screen.exitonclick()