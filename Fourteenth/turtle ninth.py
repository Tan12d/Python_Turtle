import colorsys
import turtle as t
t.bgcolor("black")
t.speed(0)
t.pensize(3)

hue =0.0
for i in range(300):
 color= colorsys.hsv_to_rgb(hue,1,1)
 t.pencolor(color)
 hue +=0.005
 t.right(i)
 t.circle(50,i)
 t.forward(i)
 t.left(91);