import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

colors = ["white", "black"]

t.penup()
t.goto(0, 0)
t.pendown()

a = 0        
angle = 0  
b = 0.6      

for i in range(800):
    color = colors[i % 2]    
    t.pencolor(color)
    x = a * math.cos(math.radians(angle))
    y = a * math.sin(math.radians(angle))
    t.goto(x, y)

 
    t.circle(a / 6, 20)

    angle += 10      
    a += b                     


t.hideturtle()
turtle.done()
