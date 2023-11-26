total = 0
counter = 0

user_input = int(input('Enter numbers: '))
while user_input != 0:
    total += user_input
    counter += 1
    user_input = int(input('Enter numbers: '))


average = total / counter
print('The sum is', total)
print('The average is', average)