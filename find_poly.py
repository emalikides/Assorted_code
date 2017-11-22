def poly(x):
	return 9*x**7 + 3*x**2 + 2*x + 5

def find_poly(poly):
	# function that finds the coefficients of a polynomial given two queries
	f1 = poly(1)
	f2 = poly(f1+1)

	lst = []
	i = 0
	c = 1
	#while c != 0 or i > 1000:
	for i in range(8):
		i += 1
		c = f2%(f1 + 1)
		lst.append(c)
		print(c)
		f2 = (f2 - c)/(f1 + 1)
	return lst

print(find_poly(poly))