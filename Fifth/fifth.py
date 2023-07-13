import turtle

turtle.bgcolor("black")
turtle.speed(60)
turtle.hideturtle()

Colors = ["yellow", "red", "yellow", "red"]

for i in range (120):
    for c in Colors:
        turtle.color(c)
        turtle.circle(100-i, 100)
        turtle.lt(90)
        turtle.circle(100-i, 100)
        turtle.rt(60)
        turtle.end_fill()

turtle.mainloop()