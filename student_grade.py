passes = 0
failures = 0

for student in range(10):

	result = int(input('Enter student result; 1 for pass, 2 for fail: '))

	if result == 1:
		passes += 1
	elif result == 2:
		failures += 1

	if result < 1 or result > 2:
		print('Invalid Input! Enter a result: 1 for pass or 2 for fail')

print('passed: ', passes)
print('failed: ', failures)

if passes >= 8:
	print('Bonus To Instructor')
