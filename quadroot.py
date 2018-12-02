import math
def quadratic(a, b, c):
	if 4*a*c-b*b < 0:
		print('no real roots')
	x1 = (-b+math.sqrt(4*a*c-b*b))/(2*a)
	x2 = (-b-math.sqrt(4*a*c-b*b))/(2*a)
	return x1, x2

roots = quadratic(1, 2, 1)
print(roots)