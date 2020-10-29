#!/bin"python3

import turtle
import random
melissa=turtle.Turtle()

turtle.Screen().bgcolor("pink")
colours=["cyan","purple","red","orange"]
melissa.color("cyan")
melissa.penup()
melissa.forward(90)
melissa.left(45)
melissa.pendown()

def branch():
  for i in range(3):
    for i in range(3):
      melissa.forward(30)
      melissa.backward(30)
      melissa.right(45)
    melissa.left(90)
    melissa.backward(30)
    melissa.left(45)
  melissa.right(90)
  melissa.forward(90)

for i in range(8):
    branch()
    melissa.left(45)

# melissa.color(random.choice(colours))


