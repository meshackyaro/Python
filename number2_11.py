digits = int(input('Enter five digit number: '))

number_one = digits // 10000;
number_two = (digits % 10000) // 1000;
number_three = (digits % 1000) // 100;
number_four = (digits % 100) // 10;
number_five = digits % 10;

print(number_one,'\t',number_two,'\t',number_three,'\t',number_four,'\t',number_five)