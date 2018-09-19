#https://www.geeksforgeeks.org/turtle-programming-python/
import turtle  #Inside_Out
wn = turtle.Screen()
wn.bgcolor("black")
skk = turtle.Turtle()
skk.color("white")

def sqrfunc(size):
	for i in range(10):
		while 1==1:
			for i in range(10):
				skk.fd(size)
				skk.left(10)
				size = size + 5

sqrfunc(10)
sqrfunc(20)
sqrfunc(30)
sqrfunc(40)
sqrfunc(50)
sqrfunc(60)
sqrfunc(70)
sqrfunc(80)
holdit = input();
