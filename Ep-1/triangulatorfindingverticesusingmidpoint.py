print("I am A Finder who gives you answer to your problems")
print("I will find you the traingle vertices points with your midpoints in the side")
print('-----------------------------------------------------------------------------')

class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def ApplyMidPointFormula(a1, a2):
	return (a1 + a2)/2

#print("Let A")
print("Please write the value of the midpoint which is between A to B")
midpoint1x = int(input("write point of x: "))
midpoint1y = int(input("write point of y: "))

print("Please write the value of the midpoint which is between B to C")
midpoint2x = int(input("write point of x: "))
midpoint2y = int(input("write point of y: "))

print("Please write the value of the midpoint which is between C to A")
midpoint3x = int(input("write point of x: "))
midpoint3y = int(input("write point of y: "))

midpoint1 = point(midpoint1x, midpoint1y)
midpoint2 = point(midpoint2x, midpoint2y)
midpoint3 = point(midpoint3x, midpoint3y)

equationAXtoBX = midpoint1.x * 2
equationBXtoCX = midpoint2.x * 2
equationCXtoAX = midpoint3.x * 2

equation4 = (equationCXtoAX + equationBXtoCX + equationAXtoBX)/2

print("Finding X Values ........")

x1 = equation4 - equationBXtoCX
x2 = equation4 - equationCXtoAX
x3 = equation4 - equationAXtoBX

print("Finding Y Values .......")

equationAYtoBY = midpoint1.y * 2
equationBYtoCY = midpoint2.y * 2
equationCYtoAY = midpoint3.y * 2

equationY4 = (equationAYtoBY + equationBYtoCY + equationCYtoAY)/2

y1 = equationY4 - equationBYtoCY
y2 = equationY4 - equationCYtoAY
y3 = equationY4 - equationAYtoBY

print("Found All Values Printing it")
print("-------------------------------")

A = point(x1, y1)
B = point(x2, y2)
C = point(x3, y3)

print("A is " + "(" + str(A.x) + "," + str(A.y) + ")")
print("B is " + "(" + str(B.x) + "," + str(B.y) + ")")
print("C is " + "(" + str(C.x) + "," + str(C.y) + ")")