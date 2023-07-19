import turtle as t
import time
t.bgcolor("white")
t.title("My first turtle file")
t.speed(2)
t.pensize(1)
t.color("red","yellow")
t.penup()
t.goto(-180,90)
t.pendown()
t.begin_fill()
for i in range(4):
 t.forward(100)
 t.right(90)
t.end_fill()

time.sleep(5)