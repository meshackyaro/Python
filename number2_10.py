number_one = int(input('Enter first number :'))
number_two = int(input('Enter second number: '))
number_three = int(input('Enter third number: '))

sum = number_one + number_two + number_three
print('The sum of the numbers is: ', sum)

average = sum / 3
print('The average of the numbers is: ', average)

product = number_one * number_two * number_three
print('The product of the numbers is: ', product)

largest = 0
smallest = number_two

if number_one > largest:
	largest = number_one

if number_two > largest:
	largest = number_two

if number_three > largest:
	largest = number_three

if number_one < smallest:
	smallest = number_one

if number_two < smallest:
	smallest = number_two

if number_three < smallest:
	smallest = number_three

print(largest, 'is the largest number')
print(smallest, 'is the smallest number')

