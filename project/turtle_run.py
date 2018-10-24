import turtle, random
import time

t = turtle.Turtle()
w = turtle.Screen()
colors  = ["red","green","blue","orange","purple","pink","yellow"]


def init():
	w.bgcolor("grey")
	shape = turtle.Turtle()


def polygon(t, l, n):
	angle = 360.0 / n
	for i in range(n):
		t.fd(l)
		t.begin_fill()
		t.lt(angle)
		t.end_fill()
 


length = 5

init()
sides = int(input("How many sides? "))
for count in range(100):
  color = random.choice(colors) #Choose a random color
  shape = turtle.Turtle()
  shape.speed(0)
  shape.pu()
  shape.setpos(-200,-200)
  shape.pd()
  # shape.forward(length)
  # shape.right(135)
  shape.color(color)
  length = length + 5
  shape.width(3)
  polygon(shape, length, sides)
  
  
w.exitonclick()