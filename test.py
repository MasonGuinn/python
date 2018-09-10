import turtle

print("Type 'start'")	#Prompt the user to type start
a = input()		#Declaring a variable and storing it as user input

if (a == "start"):		#if user types "start" this will run
	silly = turtle.Turtle()
	print ("Starting!")
	while 1 == 1:		#basic loop for a square
		silly.forward(50)	# Move forward 50 pixels
		silly.right(90)     # Rotate clockwise by 90 degrees
		silly.forward(100)	# Move forward 100 pixels
		silly.right(90)
		silly.left(90) 	
		silly.forward(55)
		silly.right(10)
		silly.forward(50)
		
	turtle.done()
else:
	print("Please type 'start'")	#Prompt the user to type start

