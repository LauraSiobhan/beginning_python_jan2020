card_list = [(3, 'diamonds'), (8, 'clubs')]

total = 0
for item in card_list:
	number = item[0]
	suit   = item[1]
	print(f'{number} of {suit}')
	total += number
	answer = input('Press enter to hit, or "s" to stay ')
	if answer == "s":
		break

print(f'My total number of points is {total}')
