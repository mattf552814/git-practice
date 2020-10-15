a = int(input('First number: '))
b = int(input('Second number: '))

import turtle
painter = turtle.Turtle()

for i in range(2):
	painter.forward(a)
	painter.right(90)
	painter.forward(b)
	painter.right(90)

wn = turtle.Screen()
wn.mainloop()