import turtle as t
import time

def curve():

    for i in range(200):
       t.right(1)
       t.forward(1)

def heart():

    t.fillcolor('red')
    # t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

def txt():
    t.up()
    t.setpos(-68,95)
    t.down()
    t.color('lightgreen')
    t.write("I Love You",font=("Verdana",12,"bold"))

heart()
txt()
t.ht()

time.sleep(15)