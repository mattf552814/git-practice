a = int(input('First number: '))
b = int(input('Second number: '))

import turtle
painter = turtle.Turtle()

painter.fillcolor(input('color: '))
painter.begin_fill()

for i in range(2):
	painter.forward(a)
	painter.right(90)
	painter.forward(b)
	painter.right(90)

painter.end_fill()

wn = turtle.Screen()
wn.mainloop()