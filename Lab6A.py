print('Enter numbers to calculate product and sum')
print('Enter done when all of the numbers have been entered')
print()

user_input = input('Enter the next number, Type \'done\' to calculate: ')
user_sum = 0
user_product = 1

list = []
while user_input != 'done':
    user_sum += int(user_input)
    list.append(user_input)
    user_product *= int(user_input)
    user_input = input('Enter the next number, Type \'done\' to calculate: ')

i = 0
while i < len(list):
    print(list[i], end= ' ')
    if i < (len(list) - 1):
        print('+', end=' ')
    i += 1

print('=', user_sum)

k = 0
while k < len(list):
    print(list[k], end= ' ')
    if k < (len(list) - 1):
        print('*', end=' ')
    k += 1
print("=", user_product)