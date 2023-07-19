import turtle as t
t.bgcolor("black")
t.speed(0)
list=["magenta","hotpink","yellow","green","orange","red"]
for i in range(100):
    t.color(list[i%5])
    t.circle(i)
    t.circle(i+1)
    

t.goto(0,-90)

for j in range(100):
    t.color(list[j%5])
    t.circle(j)
    t.circle(j+1)