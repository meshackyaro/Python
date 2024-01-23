number = int(input('Enter a number to find its factorial: '))

factorial = 1

while number > 1:
	factorial = factorial * number
	number = number - 1
print(factorial)