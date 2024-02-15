from turtle import *

def foug(n,d,a):      
	if n==0:
		forward(d)
		backward(d)
	else:    
		forward(d/3)
		foug_branches(n-1,1.25*d/3,a)

		forward(d/3)
		foug_branches(n-1,1.25*d/3,a)

		foug(n-1, 1.25*d/3, a)

		backward(2*d/3)

def foug_branches(n,d,a):
	left(a)
	foug(n,d,a)
	right(a)
	right(a)
	foug(n,d,a)
	left(a)
	
def dessin(): 
	reset()
	speed('fastest')
	color("black")
	left(90)
	up()
	backward(200)
	down()
	foug(5,200,30)
	
	

dessin()