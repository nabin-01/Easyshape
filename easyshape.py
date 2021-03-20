import turtle

a = turtle.Turtle()
s = turtle.Screen()
s.setup(width=700, height=400, startx=590, starty=0)
s.title("Interactive drawing")
x = a.xcor()
y = a.ycor()
a.color = ""
a.pensize(1)


def line(x1, y1, x2, y2):
    a.pu()
    a.setpos(x1, y1)
    a.pd()
    a.goto(x2, y2)
    a.speed(1)


def arc(r, angle):
    a.pu()
    a.goto(x, y)
    a.pd()
    a.circle(r, angle)
    a.speed(1)


def text(b, t_s, x, y):
    a.pu()
    a.goto(x, y)
    a.pd()
    a.write(b, move=False, align="left", font=("Times New Roman", t_s, "normal"))
    a.speed(1)


def settings(p_c, p_t):
    a.pencolor(p_c)
    a.pensize(p_t)
