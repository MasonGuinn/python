#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("black")
skk = turtle.Turtle()
skk.color("white")

def sqrfunc(size):
	for i in range(360):
			for i in range(90):
				skk.fd(size)
				skk.left(90.5)
				size = size + 5

sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
sqrfunc(100)
holdit = input();
