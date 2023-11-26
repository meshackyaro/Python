dog_years = int(input('Enter dog years: '))


if dog_years <= 2:
	human_year = 10.5 * dog_years
	
elif dog_years > 2:
	
	human_year = (dog_years - 2) * 4 + 21 

print('The dogs age in human years is:', human_year)