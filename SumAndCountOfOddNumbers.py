total = 0
count = 0
for number in range(1000, 5000):
	if number % 2 != 0:
		total += number
		count += 1
print(total)
print(count)
		