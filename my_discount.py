def my_discount(price, discount):
	percentage = (discount/100) * price
	discount_price = price - percentage
	return print("The new price after discount is ",+ discount_price)



price = 150
discount = 15
my_discount(price, discount)