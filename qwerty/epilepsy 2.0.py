from random import *
from turtle import *
q = Turtle()
w = Screen()
q.speed(0)
i=0
def rainbowcirc(s):
    a = randint(1,5)
    if a == 1:
        q.pencolor('red')
    if a == 2:
        q.pencolor('yellow')
    if a == 3:
        q.pencolor('blue')
    if a == 4:
        q.pencolor('green')
    if a == 5:
        q.pencolor('purple')
    q.circle(s)
    q.left(3.14)
    q.forward(s/10)
    q.right(180)
    q.circle(s)
    q.right(180)
while True:
    i+=1
    rainbowcirc(i)
w.mainloop()
