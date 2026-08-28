import turtle
import math

screen = turtle.Screen()
screen.setup(width=1400, height=1400)
screen.title("BMW Logo using Python Turtle")
screen.bgcolor("#ffffff")

t = turtle.Turtle()
t.speed(5)
t.hideturtle()

def draw_circle(radius, color, border_color=None, border_width=1):
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pensize(border_width)
    if border_color:
        t.pencolor(border_color)
    else:
        t.pencolor(color)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_quarter(radius, start_angle, color):
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)
    t.pencolor(color)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.forward(radius)
    t.left(90)
    t.circle(radius, 90)
    t.goto(0, 0)
    t.end_fill()

def draw_text(text, angle, radius, font_size):
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    t.goto(x, y - (font_size / 2))
    t.pencolor("#ffffff")
    t.write(text, align="center", font=("Arial", font_size, "bold"))

draw_circle(radius=200, color="#d3d3d3")
draw_circle(radius=190, color="#000000")
draw_circle(radius=115, color="#ffffff", border_color="#d3d3d3", border_width=2)

draw_quarter(radius=112, start_angle=0, color="#0066b2")
draw_quarter(radius=112, start_angle=90, color="#ffffff")
draw_quarter(radius=112, start_angle=180, color="#0066b2")
draw_quarter(radius=112, start_angle=270, color="#ffffff")

draw_text("B", angle=125, radius=145, font_size=32)
draw_text("M", angle=90, radius=145, font_size=32)
draw_text("W", angle=55, radius=145, font_size=32)

screen.exitonclick()
