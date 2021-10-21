# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n')
pet_name = input('Enter pet\'s name:\n')
num = int(input('Enter a number:\n'))
num = str(num)



# FIXME (2): Output two password options
password = favorite_color + " " + pet_name + " " + num
print('You entered:', password)

password1 = favorite_color + "_" + pet_name
print('\nFirst password:', password1)
password2 = num + favorite_color + num
print('Second password:', password2)
print()


# FIXME (3): Output the length of the two password options
print('Number of characters in', end= ' ')
print(password1, sep=' ', end= '')
print(":", end=' ')
print(len(password1))
print('Number of characters in', end= ' ')
print(password2, sep=' ', end= '')
print(":", end=' ')
print(len(password2))
