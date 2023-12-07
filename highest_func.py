def highest(number1, number2, number3):
	highest_number = 0
	if number1 > number2 and number1 > number3:
		highest = number1
	if number2 > number1 and number2 > number3:
		highest = number2
	if number3 > number1 and number3 > number2:
		highest = number3

print(highest_number(4, 14, 12))