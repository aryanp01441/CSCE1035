fruit_list = {
	'apple': 105,
	'bananas': 56,
	'oranges': 0
}

print('Current fruit inventory:', fruit_list)
new_fruit = input('Enter latest fruit shipment received: ')
new_fruit_quantity = int(input('Enter quantity of: '))

if new_fruit in fruit_list:
	print('Amount', new_fruit, 'in store', "=", new_fruit_quantity)
fruit_list[new_fruit] = new_fruit_quantity
print('dict_items (', fruit_list, ")")

fruit_less = input('Enter fruit being discontinued at store: ')

if fruit_less in fruit_list:
	print(fruit_less, "no longer carried in store")
	fruit_list.pop(fruit_less)
else:
	print(fruit_less, 'already not carried in store')
print('Total types of fruit in store:', len(fruit_list))