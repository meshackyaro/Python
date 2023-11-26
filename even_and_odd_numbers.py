count_even = 0
count_odd = 0
for numbers in range(1, 101):
	if numbers % 2 == 0:
		count_even += 1
	elif numbers % 2 != 0:
		count_odd += 1
print('number of even numbers: ', count_even)
print('number of odd numbers: ', count_odd)