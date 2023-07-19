from re import L
import turtle as t
t.bgcolor("black")
t.speed(0)
list=["red","green","blue"]
temp=1
for i in range(400):
    t.color(list[i%3])
    t.forward(temp)
    t.left(120)
    t.left(1)
    temp=temp+1