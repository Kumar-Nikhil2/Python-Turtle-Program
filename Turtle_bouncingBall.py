from turtle import *

wn = Screen()
wn.bgcolor("Black")

ball = Turtle()
ball.shape("circle")
ball.color('orange')
ball.speed(0)

ball.penup()
ball.goto(0,200)

y = 0
spd = 0.03

while True:

    y -= spd 
    ball.sety( ball.ycor() + y)

    if ball.ycor() < -200:
        y *= -1


wn.mainloop()    
    
