import turtle
import colorsys

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Live Weaving Neon Matrix Star")
screen.bgcolor("#040209")
screen.tracer(2, 10)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

total_steps = 360

for i in range(total_steps):
    hue = i / total_steps
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)

    t.forward(i * 1.5)
    t.left(98)
    t.forward(i * 0.5)
    t.right(15)

screen.exitonclick()

