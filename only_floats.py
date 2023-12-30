def only_floats(a, b):
	if a % 1 != 0 and b % 1 != 0:
		return 2
	elif a % 1 != 0 or b % 1 != 0:
		return 1
	else:
		return 0
	
c = only_floats(2.5, 3.5)
print (c)